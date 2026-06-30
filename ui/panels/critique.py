# critique.py

from rich.console import Group
from rich.panel import Panel
from rich.text import Text

from ui.state import UIState


def render_panel(title, critique, color):

    rows = []

    if not critique.weaknesses:

        rows.append(
            Text(
                "No critique.",
                style="green",
            )
        )

    else:

        for w in critique.weaknesses:

            rows.append(
                Text(
                    "• " + w
                )
            )

    rows.append(Text())

    rows.append(

        Text(

            f"Hallucination Risk : {critique.hallucination_risk}",

            style="bold yellow",

        )

    )

    return Panel(

        Group(*rows),

        title=title,

        border_style=color,

    )


def render_critique_a(state):

    return render_panel(

        "Critique A",

        state.critique_a,

        "blue",

    )


def render_critique_b(state):

    return render_panel(

        "Critique B",

        state.critique_b,

        "magenta",

    )