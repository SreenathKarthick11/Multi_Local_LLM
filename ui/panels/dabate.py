# ui/panels/debate.py
from rich.panel import Panel
from rich.console import Group
from rich.text import Text

from ui.state import UIState
from ui.widgets import confidence
from ui.scroll import windowed


def build_agent(title, agent, color, console=None, viewport=None, scroll_state=None):
    content = Group(
        Text(agent.status, style="bold warning"),
        Text(),
        Text(agent.answer or "..."),
        Text(),
        confidence(agent.confidence),
    )

    if console and viewport and scroll_state:
        width, height = viewport
        content, more_above, more_below = windowed(console, content, width, height, scroll_state)
        title = ("▲ " if more_above else "") + title + (" ▼" if more_below else "")

    return Panel(content, title=title, border_style=color)


def render_agent_a(state: UIState, console=None, viewport=None, scroll_state=None):
    return build_agent("Agent A", state.agent_a, "color_a", console, viewport, scroll_state)


def render_agent_b(state: UIState, console=None, viewport=None, scroll_state=None):
    return build_agent("Agent B", state.agent_b, "color_b", console, viewport, scroll_state)