from rich.console import Console

from ui.theme import theme

console = Console(
    theme=theme,
    soft_wrap=True,
    highlight=False,
)