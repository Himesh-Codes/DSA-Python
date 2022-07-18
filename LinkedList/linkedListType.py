#!/usr/bin/env python3
"""
Linked List Types Classes
"""

from dataclasses import dataclass
from typing import Union

@dataclass
class TraversalItem():
    position: int = 0
    data: Union[str, int] = ''