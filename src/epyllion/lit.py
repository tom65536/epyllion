"""
This module generates Code from MarkDown sources.
"""

from __future__ import annotations

import logging
import pathlib
import shlex
from dataclasses import dataclass
from typing import Any

import mistune
from mistune.core import BlockState
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
        super().__init__()
        self._context = ctx

    def block_code(self, token: dict[str, Any], state: BlockState) -> str:
        attrs = token.get("attrs", {})
        info = attrs.get("info", "")
        args = shlex.split(info)
        result = super().block_code(token, state)
        result += "\n" + repr(args) + "\n"
        return result


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
        with pathlib.Path("epyllion-out.md").open("w", encoding="utf-8") as out:
            out.write("---\n")
            out.write("file-name: ")
            out.write(file_name)
            out.write("\n")
            out.write("---\n")
            out.write(mddoc)


# We parse the extra info passed to fenced code blocks
