"""
Circular Queue Factory : Optimise memory usage, circulate the head & tail pointers in a queue
First In First Out (FIFO) 
Enqueue: Add an element to the end of the queue
Dequeue: Remove an element from the front of the queue
IsEmpty: Check if the queue is empty
IsFull: Check if the queue is full
Peek: Get the value of the front of the queue without removing it

Complexity
--------------------
The complexity of the enqueue and dequeue operations of a circular queue is O(1) for (array implementations).

Applications
--------------------
CPU scheduling
Memory management
Traffic Management
"""

from re import T
from tkinter import E
from typing import TypeVar
from queueType import OperationType

MAX_SIZE = 'maxSize'
STACK = TypeVar('STACK', list, set)

class CircularQueueFactory():
    def __init__(self, **kwargs):
        self.__maxStackSize = kwargs[MAX_SIZE] if MAX_SIZE in kwargs else 100
        self.__queue: STACK = list('#') * self.__maxStackSize
        self.__head = -1
        self.__tail = -1
    
    def enqueue(self, item):
        # check mod of tail lets say 4+1 %5 is equal 0 and head is in 0
        if (self.__tail + 1) % self.__maxStackSize == self.__head:
            raise OverflowError('Queue is full')
        elif self.__head == -1:
            self.__head, self.__tail = 0, 0
            self.__queue[self.__tail] =  item
        else:
            self.__tail = (self.__tail + 1) % self.__maxStackSize
            self.__queue[self.__tail] =  item
            
    def dequeue(self):
        if self.__head == -1:
            raise BufferError('Queue is empty')
        # check head + 1 mod, let's say head in 4+1 % 5 = 0, then made last element pop
        elif (self.__head+1) % self.__maxStackSize == self.__tail:
            popItem = self.__queue[self.__head]
            self.__tail, self.__head = -1, -1
            return popItem
        else:
            popItem = self.__queue[self.__head]
            self.__head = (self.__head + 1) % self.__maxStackSize
            return popItem
            
    def printQueue(self):
        if self.__head == -1:
            print('Empty Queue')
        elif self.__tail >= self.__head:
            for index in range(self.__head, self.__tail + 1):
                print(self.__queue[index], end=' ')
            print('')
        else:
            for index in range(self.__head, self.__maxStackSize):
                 print(self.__queue[index], end=' ')
            for index in range(0, self.__tail + 1):
                 print(self.__queue[index], end=' ')
                
# Testing
circularQueue = CircularQueueFactory(maxSize = 5)
circularQueue.printQueue()
try:
    circularQueue.enqueue('Rob')
    circularQueue.enqueue('Geo')
    circularQueue.enqueue('Sara')
    circularQueue.enqueue('Reena')
    circularQueue.enqueue('Amaya')
    circularQueue.enqueue('Ivan')
except:
    pass
print('Queue Items:', flush=True)
circularQueue.printQueue()

print(circularQueue.dequeue())
print(circularQueue.dequeue())
print(circularQueue.dequeue())
print('Queue Items:', flush=True)
circularQueue.printQueue()