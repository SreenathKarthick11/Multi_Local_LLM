from rich.console import Console
from .theme import theme

console = Console(
    theme=theme,
    color_system="truecolor",   # don't let Rich auto-detect and guess wrong
    force_terminal=True, 
    # record=False,
)