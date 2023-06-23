"""
Define the `python` chunk command
"""

import click

import click_extra


@click.command()
@click.pass_context
@click_extra.config_option
def python(ctx) -> None:
    """
    Process code chunk for language Python
    """
