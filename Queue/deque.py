"""
Double Ended Queue Factory : Insertion and removal of elements can either be performed from the front or the rear.

Types of Deque
- Input Restricted Deque
    In this deque, input is restricted at a single end but allows deletion at both the ends.
- Output Restricted Deque
    In this deque, output is restricted at a single end but allows insertion at both the ends.

Complexity
--------------------
The complexity of the all of operations of a dequeue is O(1) for (array implementations).

Applications
--------------------
Store browser history
Undo operations
"""

from re import T
import sys
from tkinter import E
from typing import TypeVar

MAX_SIZE = 'maxSize'
STACK = TypeVar('STACK', list, set)

class DeQueueFactory():
    def __init__(self):
        self.__queue: STACK  = []
    
    def addFront(self, item):
        self.__queue.insert(0, item)
        
    def addRear(self, item):
        self.__queue.append(item)

    def checkEmpty(self) -> bool:
        return len(self.__queue) <= 0
    
    def size(self):
        return len(self.__queue)

    def removeFront(self):
        if len(self.__queue) < 1:
            raise BufferError('Array is already empty')
        return self.__queue.pop(0)
    
    def removeRear(self):
        if len(self.__queue) < 1:
            raise BufferError('Array is already empty')
        return self.__queue.pop()
    
    def printQueue(self):
        for item in self.__queue:
            print(item)
        
# Testing
deque = DeQueueFactory()
try:
    deque.removeFront()
    deque.removeFront()
except:
    print(f'Error: {sys.exc_info()[1]}')

deque.addFront(12)
deque.addRear('Left')
deque.addRear('Right')
deque.addFront(15)
deque.addFront('Start')
deque.printQueue()