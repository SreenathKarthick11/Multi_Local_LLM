# router.py

from rich.console import Group
from rich.panel import Panel
from rich.text import Text

from ui.state import UIState
from ui.widgets import status, badge, confidence


def render_router(state: UIState):

    router = state.router

    items = []

    items.append(status(router.status, "running"))

    items.append(Text())

    items.append(
        status(
            "Web Search",
            "success" if router.use_web else "waiting",
        )
    )

    items.append(
        status(
            "Local RAG",
            "success" if router.use_rag else "waiting",
        )
    )

    items.append(
        status(
            "Python Tool",
            "success" if router.use_python else "waiting",
        )
    )

    items.append(Text())

    items.append(confidence(router.confidence))

    if router.reason:

        items.append(Text())

        items.append(
            Text(router.reason, style="dim")
        )

    return Panel(
        Group(*items),
        title="Router",
        border_style="color_router",
    )