from rich.theme import Theme

theme = Theme(
    {
        # Titles
        "title": "bold cyan",

        # Agent colours
        "agent_a": "bold bright_blue",
        "agent_b": "bold bright_magenta",

        # Different sections
        "router": "bright_yellow",
        "resource": "bright_green",
        "judge": "bright_red",

        # Status
        "success": "green",
        "warning": "yellow",
        "danger": "red",

        # Text
        "muted": "grey62",
        "info": "cyan",

        # Confidence
        "high": "green",
        "medium": "yellow",
        "low": "red",

        # Borders
        "panel": "grey42",
    }
)