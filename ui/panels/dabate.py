# debate.py

from rich.columns import Columns
from rich.panel import Panel
from rich.console import Group
from rich.text import Text

from ui.state import UIState

from ui.widgets import confidence


def build_agent(title, agent, color):

    return Panel(

        Group(

            Text(
                agent.status,
                style="bold yellow",
            ),

            Text(),

            Text(
                agent.answer or "...",
            ),

            Text(),

            confidence(
                agent.confidence
            ),

        ),

        title=title,

        border_style=color,

    )


def render_debate(state: UIState):

    return Columns(

        [

            build_agent(
                "Agent A",
                state.agent_a,
                "color_a",
            ),

            build_agent(
                "Agent B",
                state.agent_b,
                "color_b",
            ),

        ],

        equal=True,

        expand=True,

    )