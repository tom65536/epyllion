"""
Entry point for the chunk cli.
"""
import shlex

import click

from .chunk_commands.python_chunk import python
from .context import Context


@click.group()
@click.pass_context
def chunks(ctx) -> None:
    """
    Parse the extra info passed to fenced code blocks using click.
    """

chunks.add_command(python)

def configure_chunk(info: str, ctx: LitContext) -> Callable[[str], str]:
    """
    Create and configure a processor for a given chunk info.

    Arguments:
    ----------
    - info: the chunk info
    - ctx: the context
    """
    arg_list: list[str] = shlex.split(info,
                                      comments=True,
                                      posix = True)