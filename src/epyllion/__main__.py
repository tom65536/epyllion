from __future__ import annotations

import click
from click import echo

from .lit import Lit


@click.command
@click.argument("input", type=click.File("r"))
def main(input) -> None:
    """
    Wraps the main program.
    """
    lit = Lit()
    lit.add_markdown(input.read(), "<file>.md")
    echo("ALL DONE")


if __name__ == "__main__":
    main()
