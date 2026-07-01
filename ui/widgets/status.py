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
        "running": "warning",
        "success": "success",
        "failed": "error",
        "waiting": "dim",
    }

    return Text(
        f"{icons[state]} {text}",
        style=colors[state],
    )