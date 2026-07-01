from rich.text import Text


def status(text: str, state: str = "running") -> Text:
    """
    running
    success
    failed
    waiting
    """

    icons = {
        "running": "...",
        "success": "✓",
        "failed": "✗",
        "waiting": "•",
    }

    colors = {
        "running": "yellow",
        "success": "green",
        "failed": "red",
        "waiting": "grey70",
    }

    return Text(
        f"{icons[state]} {text}",
        style=colors[state],
    )