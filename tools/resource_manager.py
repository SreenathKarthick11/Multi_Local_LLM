from models import ResourceContext
from tools.search_helper import get_evidence
from tools.tool_helper import get_tool
from rag.rag_helper import get_retrieval



def build_context(web: str,rag: str,tools: list,):
    return ResourceContext(
        web_evidence=web,
        rag_evidence=rag,
        tools=tools,
    )


def get_resources(question: str):

    web, search_decision = get_evidence(question)
    tool = get_tool(question)
    rag,retrive_decision = get_retrieval(question)

    context = build_context(
        web=web,
        rag=rag,
        tools=[tool] if tool else [],
    )

    return context, search_decision,retrive_decision

def format_resource(resource):

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