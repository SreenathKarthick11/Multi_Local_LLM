# judge.py

from rich.console import Group
from rich.panel import Panel
from rich.text import Text

from ui.state import UIState
from ui.widgets import confidence


def render_judge(state: UIState):

    judge = state.judge

    return Panel(

        Group(

            Text(

                f"Winner : {judge.winner}",

                style="bold green",

            ),

            Text(),

            confidence(

                judge.confidence

            ),

            Text(),

            Text(

                judge.reasoning,

            ),

        ),

        title="Judge",

        border_style="red",

    )