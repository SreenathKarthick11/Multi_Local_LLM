from rich.spinner import Spinner


def thinking(text="Thinking..."):

    return Spinner(
        "dots",
        text=text,
        style="cyan",
    )