from rich.table import Table


def info_table(data: dict):

    table = Table.grid(expand=True)

    table.add_column(style="bold cyan", ratio=1)
    table.add_column(ratio=3)

    for k, v in data.items():
        table.add_row(k, str(v))

    return table