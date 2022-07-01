#!/usr/bin/env python3
"""
Queue Types Classes
"""

from enum import Enum

class OperationType(Enum):
    ENQUEUE = 'add'
    DEQUEUE = 'remove'
        