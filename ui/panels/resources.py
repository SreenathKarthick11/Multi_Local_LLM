# resources.py

from rich.console import Group
from rich.panel import Panel
from rich.text import Text

from ui.state import UIState


def section(title, body):

    if not body:
        body = "None"

    return Group(
        Text(title, style="bold cyan"),
        Text(body),
        Text(),
    )


def render_resources(state: UIState):

    res = state.resources

    return Panel(

        Group(

            section(
                "Web",
                res.web,
            ),

            section(
                "RAG",
                res.rag,
            ),

            section(
                "Tools",
                res.tools,
            ),

        ),

        title="Resources",

        border_style="green",

    )