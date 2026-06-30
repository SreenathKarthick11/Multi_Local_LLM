from rich.text import Text


def badge(label: str, color="cyan"):

    t = Text()

    t.append(" ")
    t.append(label.upper(), style=f"bold {color}")
    t.append(" ")

    return t