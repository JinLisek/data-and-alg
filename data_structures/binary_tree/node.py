from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: int
    left: Optional[Node] = None
    right: Optional[Node] = None


@dataclass
class ColorNode:
    value: int
    is_red: bool
    left: Optional[ColorNode] = None
    right: Optional[ColorNode] = None
    parent: Optional[ColorNode] = None

    def is_uncle_black(self) -> bool:
        return True
