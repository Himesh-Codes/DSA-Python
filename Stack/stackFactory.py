#!/usr/bin/env python3
"""
Stack Factory 
LIFO (Last In First Out) Principle 
Push: Add an element to the top of a stack
Pop: Remove an element from the top of a stack
IsEmpty: Check if the stack is empty
IsFull: Check if the stack is full
Peek: Get the value of the top element without removing it

Complexity
--------------------
Stack time complexity O(1)

Applications
--------------------
In browsers - The back button in a browser saves all the URLs you have visited previously in a stack
In compilers - Compilers use the stack to calculate the value of expressions like 2 + 4 / 5 * (7 - 9) by 
converting the expression to prefix or postfix form.
"""

import sys
from typing import TypeVar


ARRAY_INIT_VAL = 'initialValue'
MAX_SIZE = 'maximumSize' 
STACK = TypeVar('STACK', list, set)

class StackFactory():
    def __init__(self, **kwargs):
        self.__stack: STACK = kwargs[ARRAY_INIT_VAL] if ARRAY_INIT_VAL in kwargs else []
        self.__maxStackSize = kwargs[MAX_SIZE] if MAX_SIZE in kwargs else 100
        self.__top = -1
    
    def checkStackEmpty(self) -> bool:
        return len(self.__stack) == 0
    
    def pushStack(self, value):
        if len(self.__stack) > self.__maxStackSize:
            raise OverflowError('Maximum Stacksize Exceeds')
        else:   
            self.__stack.append(value)
            self.__top += 1
        
    def popStack(self):
        if self.__top == -1:
            raise BufferError('Stack is already empty')
        else:
            self.__stack.pop()
            self.__top -= 1
    
    def printItems(self):
        for item in self.__stack:
            print(item)
            
# Testing
stack = StackFactory()
print(stack.checkStackEmpty())
try:
    stack.popStack()
except:
    print(f'Error: {sys.exc_info()[1]}')

try:
    stack.pushStack(10)
    stack.pushStack('Good')
except:
    print(f'Error: {sys.exc_info()[1]}')

stack.printItems()