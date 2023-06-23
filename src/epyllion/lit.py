"""
This module generates Code from MarkDown sources.
"""

from __future__ import annotations

import logging
import pathlib
import shlex
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

import mistune
from mistune.core import BlockState
from mistune.renderers.markdown import MarkdownRenderer, fenced_re

from .context import LitContext

LOGGER = logging.getLogger(__name__)

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
        try:
            args = shlex.split(info)
            chunks.main(args, standalone_mode=False)
        except Exception as ex:
            pass
        result = super().block_code(token, state)
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



def _fence(info, code, marker) -> str:
    if code and code[-1] != "\n":
        code += "\n"

    if not marker:
        marker = _get_fenced_marker(code)
    return marker + info + "\n" + code + marker + "\n\n"


def _get_fenced_marker(code):
    found = fenced_re.findall(code)
    if not found:
        return "```"

    ticks = []  # `
    waves = []  # ~
    for s in found:
        if s[0] == "`":
            ticks.append(len(s))
        else:
            waves.append(len(s))

    if not ticks:
        return "```"

    if not waves:
        return "~~~"
    return "`" * (max(ticks) + 1)
