"""
Defines a context object for tangling.
"""
from dataclasses import dataclass
from typing import Callable


@dataclass
class LitContext:
    """
    Context for the weave/tangle process
    """

    chunk_handler: Callable[[str], str] = id
