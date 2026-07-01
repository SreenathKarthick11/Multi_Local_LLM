# ui/panels/router.py
from rich.console import Group
from rich.panel import Panel
from rich.text import Text

from ui.state import UIState
from ui.widgets import status, confidence
from ui.scroll import windowed


def render_router(state: UIState, console=None, viewport=None, scroll_state=None):
    router = state.router

    items = [
        status(router.status, "running"),
        Text(),
        status("Web Search", "success" if router.use_web else "waiting"),
        status("Local RAG", "success" if router.use_rag else "waiting"),
        status("Python Tool", "success" if router.use_python else "waiting"),
        Text(),
        confidence(router.confidence),
    ]
    if router.reason:
        items += [Text(), Text(router.reason, style="dim")]

    content = Group(*items)
    title = "Router"

    if console and viewport and scroll_state:
        width, height = viewport
        content, more_above, more_below = windowed(console, content, width, height, scroll_state)
        title = ("▲ " if more_above else "") + title + (" ▼" if more_below else "")

    return Panel(content, title=title, border_style="color_router")