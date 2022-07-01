#!/usr/bin/env python3
"""
Queue Factory 
First In First Out (FIFO) 
Enqueue: Add an element to the end of the queue
Dequeue: Remove an element from the front of the queue
IsEmpty: Check if the queue is empty
IsFull: Check if the queue is full
Peek: Get the value of the front of the queue without removing it

Complexity
--------------------
The complexity of enqueue and dequeue operations in a queue using an array is O(1)
POP : complexity might be O(n) depending on the position of the item to be popped.

Applications
--------------------
CPU scheduling, Disk Scheduling
The queue is used for synchronization. For example: IO Buffers, pipes, file IO, etc
Call Center phone systems use Queues to hold people calling them in order.
"""

from typing import TypeVar
from queueType import OperationType

MAX_SIZE = 'maxSize'
STACK = TypeVar('STACK', list, set)


class QueueFactory():
    def __init__(self, **kwargs):
        self.__queue: STACK = list()
        self.__maxStackSize = kwargs[MAX_SIZE] if MAX_SIZE in kwargs else 100
        self.__front = -1
        self.__rear = -1
    
    # add to the end of the queue
    def enqueue(self, item):
        if(self.__maxStackSize > len(self.__queue)):
            self.__manageQueuePointers(OperationType.ENQUEUE)
            self.__queue[self.__rear] = item
        else:
            raise OverflowError('Maximum size exceeds')
            
    # remove from front of queue
    def dequeue(self):
        if len(self.__queue) > 0:
            popItem =  self.__queue.pop(0)
            self.__manageQueuePointers(OperationType.ENQUEUE)
            return popItem
        else:
            raise BufferError('Queue is empty')    
        
    # check empty
    def checkEmpty(self) -> bool:
        if len(self.__queue) == 0:
            return True
        else:
            return False
            
    def __manageQueuePointers(self, type: OperationType):
        if type == OperationType.ENQUEUE:
            if self.__front == -1: self.__front = 0 
            self.__rear += 1
        elif type == OperationType.DEQUEUE:
            self.__rear -= 1
            if self.checkEmpty(): self.__front, self.__rear = -1
            