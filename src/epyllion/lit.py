"""
This module generates Code from MarkDown sources.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

import mistune
from mistune.renderers.markdown import MarkdownRenderer

LOGGER = logging.getLogger(__name__)


@dataclass
class LitContext:
    """
    Context for the weave/tangle process
    """

    dummy: int = 0


class LitRenderer(MarkdownRenderer):
    """
    Derived renderer for the weave/tangle process.
    """

    def __init__(self, ctx: LitContext) -> None:
        """
        Initialize a new instancen

        Arguments:
        ----------

        ctx: the context for storing code scratches
        """
        super().__init__(self)
        self._context = ctx


class Lit:
    """
    Document processor.
    """

    _ctx: LitContext = LitContext()
    _markdown = mistune.create_markdown(renderer=LitRenderer(_ctx))

    def add_markdown(self, src: str, file_name: str) -> None:
        """
        Add some markdown document to the processing.
        """
        mddoc: str = self._markdown(src)
        LOGGER.info(mddoc)
        LOGGER.info(file_name)
