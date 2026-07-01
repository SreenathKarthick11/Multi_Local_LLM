from rich.layout import Layout
from rich.panel import Panel
from rich.console import Group
from rich.text import Text

from ui.widgets import (
    status,
    confidence,
    debate_progress,
)


def build_layout():

    layout = Layout(name="root")

    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=1),
    )

    layout["body"].split_column(
        Layout(name="top", ratio=3),
        Layout(name="middle", ratio=2),
        Layout(name="bottom", ratio=1),
    )

    layout["top"].split_row(
        Layout(name="router", ratio=1),
        Layout(name="resources", ratio=1),
        Layout(name="debate", ratio=2),
    )

    layout["middle"].split_row(
        Layout(name="critique_a"),
        Layout(name="critique_b"),
    )

    layout["bottom"].split_row(
        Layout(name="judge"),
        Layout(name="runtime"),
    )

    return layout


def demo_layout():

    layout = build_layout()

    layout["header"].update(
        Panel(
            Text(
                "Local LLM Multi-Agent Debate",
                justify="center",
                style="title",
            )
        )
    )

    layout["router"].update(
        Panel(
            Group(
                status("RAG Retrieval", "success"),
                status("Web Search", "failed"),
                status("Python Tool", "failed"),
                Text(""),
                Text(
                    "Retrieved 3 document chunks",
                    style="green",
                ),
            ),
            title="Resources",
            border_style="green",
        )
    )

    layout["debate"].update(
        Panel(
            Group(
                Text("Agent A", style="agent_a"),
                Text("Rome is the capital of Italy."),
                Text(""),
                Text("Agent B", style="agent_b"),
                Text("I agree. Rome is correct."),
            ),
            title="Debate",
            border_style="cyan",
        )
    )

    layout["critique_a"].update(
        Panel(
            Group(
                Text("✓ No hallucinations", style="green"),
                Text("✓ Good reasoning", style="green"),
                Text("! Could provide citations", style="yellow"),
            ),
            title="Critique A",
            border_style="blue",
        )
    )

    layout["critique_b"].update(
        Panel(
            Group(
                Text("✓ No hallucinations", style="green"),
                Text("✓ Good reasoning", style="green"),
                Text("! Could provide citations", style="yellow"),
            ),
            title="Critique B",
            border_style="magenta",
        )
    )

    layout["judge"].update(
        Panel(
            Group(
                Text(
                    "Winner: Agent A",
                    style="bold green",
                ),
                Text(""),
                confidence(0.92),
            ),
            title="Judge",
            border_style="red",
        )
    )

    layout["runtime"].update(
        Panel(
            debate_progress(2, 3),
            title="Runtime",
            border_style="cyan",
        )
    )

    layout["footer"].update(
        Text(
            "Press Ctrl+C to exit",
            justify="center",
            style="dim",
        )
    )

    return layout