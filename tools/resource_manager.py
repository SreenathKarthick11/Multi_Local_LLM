from concurrent.futures import ThreadPoolExecutor

from models import ResourceContext, ToolResult
from tools.resource_router import route_resources

from tools.search import search_web
from rag.retriever import retrieve_text
from tools.python_tool import python_tool

from ui.emitter import emit
from ui.events import RouterEvent, ResourceEvent

def build_context(
    web: str,
    rag: str,
    tools: list[ToolResult],
):
    return ResourceContext(
        web_evidence=web,
        rag_evidence=rag,
        tools=tools,
    )


def _run_web(route):
    if not route.use_web:
        return ""

    try:
        return search_web(route.web_query)
    except Exception:
        return ""


def _run_rag(route):
    if not route.use_rag:
        return ""

    try:
        return retrieve_text(route.rag_query)
    except Exception:
        return ""


def _run_tool(route):
    if not route.use_tool:
        return None

    if route.tool_name == "python":
        try:
            output = python_tool(route.tool_input)

            return ToolResult(
                tool_name="python",
                tool_input=route.tool_input,
                output=output,
            )

        except Exception as e:
            return ToolResult(
                tool_name="python",
                tool_input=route.tool_input,
                output=f"Python Error: {e}",
            )

    return None


def get_resources(question: str):

    route = route_resources(question)

    with ThreadPoolExecutor(max_workers=3) as executor:
        web_future = executor.submit(_run_web, route)
        rag_future = executor.submit(_run_rag, route)
        tool_future = executor.submit(_run_tool, route)

        web = web_future.result()
        rag = rag_future.result()
        tool = tool_future.result()

    context = build_context(
        web=web,
        rag=rag,
        tools=[tool] if tool else [],
    )

    emit(RouterEvent(
        status="Routed",
        use_web=route.use_web,
        use_rag=route.use_rag,
        use_python=bool(route.use_tool and route.tool_name == "python"),
        confidence=route.confidence,
        reason=route.reason,
    ))

    emit(ResourceEvent(
        web=context.web_evidence or "",
        rag=context.rag_evidence or "",
        tools="\n".join(f"{t.tool_name}: {t.output}" for t in context.tools),
    ))

    return context, route


def format_resource(resource: ResourceContext):

    tools = "\n".join(
        f"""
Tool: {tool.tool_name}
Input: {tool.tool_input}
Output: {tool.output}
"""
        for tool in resource.tools
    ) or "None"

    return (
        resource.web_evidence or "None",
        resource.rag_evidence or "None",
        tools,
    )


def format_resources(resource_bank):

    web = []
    rag = []
    tools = []

    for resource in resource_bank:

        w, r, t = format_resource(resource)

        if w != "None":
            web.append(w)

        if r != "None":
            rag.append(r)

        if t != "None":
            tools.append(t)

    return (
        "\n\n".join(web) or "None",
        "\n\n".join(rag) or "None",
        "\n\n".join(tools) or "None",
    )