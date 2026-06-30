# runtime.py

from rich.console import Group
from rich.panel import Panel
from rich.text import Text

from ui.state import UIState

from ui.widgets import debate_progress


def render_runtime(state: UIState):

    run = state.runtime

    return Panel(

        Group(

            debate_progress(

                run.round_number,

                run.max_rounds,

            ),

            Text(),

            Text(

                f"Elapsed : {run.elapsed_seconds:.2f}s"

            ),

            Text(

                f"Stop : {run.stop_reason or '-'}"

            ),

        ),

        title="Runtime",

        border_style="cyan",

    )