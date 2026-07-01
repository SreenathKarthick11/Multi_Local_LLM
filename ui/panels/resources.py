# ui/panels/resources.py
from rich.console import Group
from rich.panel import Panel
from rich.text import Text

from ui.state import UIState
from ui.scroll import windowed


def section(title, body):
    if not body:
        body = "None"
    return Group(Text(title, style="bold cyan"), Text(body), Text())


def render_resources(state: UIState, console=None, viewport=None, scroll_state=None):
    res = state.resources

    content = Group(
        section("Web", res.web),
        section("RAG", res.rag),
        section("Tools", res.tools),
    )
    title = "Resources"

    if console and viewport and scroll_state:
        width, height = viewport
        content, more_above, more_below = windowed(console, content, width, height, scroll_state)
        title = ("▲ " if more_above else "") + title + (" ▼" if more_below else "")

    return Panel(content, title=title, border_style="color_resources")