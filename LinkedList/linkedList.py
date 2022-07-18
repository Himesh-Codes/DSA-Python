"""
Singly Linked List Factory : Each node stores the data and the address of the next node.

Linked lists can be of multiple types: singly, doubly, and circular linked list.

Traversal - access each element of the linked list
Insertion - adds a new element to the linked list
Deletion - removes the existing elements
Search - find a node in the linked list
Sort - sort the nodes of the linked list

Complexity
--------------------
 	        Worst case	Average Case
Search	        O(n)	    O(n)
Insert	        O(1)	    O(1)
Deletion	    O(1)	    O(1)

Applications
--------------------
Dynamic memory allocation
Implemented in stack and queue
In undo functionality of softwares
Hash tables, Graphs
"""

import sys
from typing import Optional, TypeVar, Union
from linkedListType import TraversalItem

TypeNode = TypeVar('TypeNode', bound='Node')
class Node():
    def __init__(self, item):
        self.__data = item
        self.__next = None
    
    def setNext(self, node: Optional[TypeNode] = None):
        self.__next = node
    
    def getNext(self):
       return self.__next
        
    def getData(self):
        return self.__data
    
    def setData(self, data):
        self.__data = data
    
class LinkedListFactory():
    def __init__(self):
        self.__head: Node = None
        
    def insertFromFront(self, data):
        newNode = Node(data)
        newNode.setNext(self.__head)
        self.__head = newNode
        
    def insertAfter(self, data, previousNode: Node):
        if isinstance(previousNode, Node):
            newNode = Node(data)
            referenceNext: Node = previousNode.getNext()
            previousNode.setNext(newNode)
            newNode.setNext(referenceNext)
        else:
            return TypeError('Not a type of class node.')
        
    def insertEnd(self, data):
        newNode = Node(data)

        if self.__head == None:
            self.__head = newNode
        else:
            last = self.findLast()
            last.setNext(newNode)
            
    def findLast(self):
        last = self.__head
        # get the last node, iterate until next is None
        while(last.getNext()):
            last = last.getNext()         
        return last
    
    def deleteFromFront(self):
        if self.__head is not None:
            nextHead = self.__head.getNext()
            # memory management
            del self.__head
            self.__head = nextHead
        
    # custom data class type in python
    def deleteFromMiddle(self, item: TraversalItem):
        node: Node
        position: int
        if item.data:
            position = self.getItemByTraversal(None, item.data, True)
        elif item.position:
            position = item.position
        
        # get node before that position
        node: Node = self.getItemByTraversal(position - 1)
        if node and node == self.__head:
            self.__head == None
        elif node:
            # since the no reference points to object of delete node VM python delete it
            node.setNext(node.getNext().getNext())
    
    def deleteFromEnd(self):
        if self.__head is not None:
            currentNode = self.__head
            # check next available for head
            if self.__head.getNext():
                while(currentNode.getNext().getNext() is not None):
                    currentNode = currentNode.getNext()
                    if not currentNode.getNext(): break
                        
                if self.__head == currentNode and self.__head.getNext() is None:
                    self.__head = None
                else:
                    currentNode.setNext(None)
            # if head is needed to be deleted make head none
            else:
                self.__head = None
                

    # multiple type annotation - Union
    def getItemByTraversal(self, position=None, item=None, getPosition: bool=False) -> Union[Node,int]:
        currentNode = self.__head
        if position:
            # Iteration happens until the position
            for index in range(1, position):
                currentNode = currentNode.getNext()
        elif item:
            itemPosition = 1
            while(currentNode.getData() != item):
                currentNode = currentNode.getNext()
                itemPosition += 1
            if getPosition:
                return itemPosition
        
        return currentNode
    
    # bubble sort algorithm for linkedlist sort
    def bubbleSortLinkedList(self):
        currentNode = self.__head
        if currentNode == None:
            return None
        else:
            try:
                while currentNode is not None: 
                    indexNode = currentNode.getNext()
                    while indexNode is not None:
                        if indexNode.getData() < currentNode.getData():
                            indexNodeData = indexNode.getData()
                            indexNode.setData(currentNode.getData())
                            currentNode.setData(indexNodeData)
                        indexNode = indexNode.getNext()
                    currentNode = currentNode.getNext()
            except:
                print(f'Error: {sys.exc_info()[1]}')
            

    
    def printList(self):
        currentNode = self.__head
        if currentNode:
            while(currentNode.getNext()):
                print(currentNode.getData())
                currentNode = currentNode.getNext()
            print(currentNode.getData())
        
# Testing 
linkedList = LinkedListFactory()
linkedList.insertFromFront(12)
linkedList.insertFromFront('IG')
linkedList.insertFromFront(323)
linkedList.printList()
print('---New list----')
linkedList.deleteFromEnd()
linkedList.printList()
linkedList.insertAfter('Tiii', linkedList.getItemByTraversal(None, 'IG'))
linkedList.printList()
print('---New list----')
linkedList.insertAfter('Yekl', linkedList.getItemByTraversal(None, 'IG'))
linkedList.printList()
print('---New list----')
item: TraversalItem = TraversalItem(position=2)
linkedList.deleteFromMiddle(item)
linkedList.printList()
linkedList.deleteFromEnd()
linkedList.deleteFromEnd()
linkedList.deleteFromEnd()
linkedList.deleteFromEnd()
print('----Empty list----')
linkedList.printList()
print('----New list----')
linkedList.insertFromFront(12)
linkedList.insertFromFront(342)
linkedList.insertFromFront(9)
linkedList.insertFromFront(999)
linkedList.printList()
linkedList.bubbleSortLinkedList()
print('----Sorted list----')
linkedList.printList()