from rich.progress_bar import ProgressBar
from rich.console import Group
from rich.text import Text


def debate_progress(round_now: int, total: int):

    percent = round_now / total

    return Group(
        Text(
            f"Round {round_now}/{total}",
            style="bold cyan",
        ),
        ProgressBar(
            total=100,
            completed=int(percent * 100),
            width=40,
        ),
    )