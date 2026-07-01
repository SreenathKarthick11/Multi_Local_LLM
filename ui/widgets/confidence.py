from rich.console import Group
from rich.progress_bar import ProgressBar
from rich.text import Text


def confidence(score: float):

    score = max(0.0, min(1.0, score))

    label = Text(
        f"{score*100:.1f}% confidence",
        style="title",
    )

    bar = ProgressBar(
        total=100,
        completed=int(score * 100),
        width=30,
    )

    return Group(label, bar)