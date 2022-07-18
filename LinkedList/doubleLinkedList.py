"""
Double Linked List Factory : Each node stores the data and the address of the next and previous node.

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
# custom type declaration
TypeNode = TypeVar('TypeNode', bound='Node')
class Node():
    def __init__(self, item):
        self.__data = item
        self.__next = None
        self.__prev = None
    
    def setNext(self, node: Optional[TypeNode] = None):
        self.__next = node
        
    def setPrev(self, node: Optional[TypeNode] = None):
        self.__prev = node
    
    def getNext(self):
       return self.__next
   
    def getPrev(self):
        return self.__prev
        
    def getData(self):
        return self.__data
    
    def setData(self, data):
        self.__data = data
    
class DoubleLinkedListFactory():
    def __init__(self):
        self.__head: Node = None
        
    def insertFromFront(self, data):
        newNode = Node(data)
        newNode.setNext(self.__head)
        newNode.setPrev(None)
        if self.__head is not None:
            self.__head.setPrev(newNode)
        self.__head = newNode
        
    def insertAfter(self, data, previousNode: Node):
        if isinstance(previousNode, Node):
            newNode = Node(data)
            referenceNext: Node = previousNode.getNext()
            previousNode.setNext(newNode)
            newNode.setNext(referenceNext)
            newNode.setPrev(previousNode)
            referenceNext.setPrev(newNode)
        else:
            return TypeError('Not a type of class node.')
        
    def insertEnd(self, data):
        newNode = Node(data)

        if self.__head == None:
            self.__head = newNode
        else:
            last = self.findLast()
            last.setNext(newNode)
            newNode.setPrev(last)
            
    def findLast(self):
        last = self.__head
        # get the last node, iterate until next is None
        while(last.getNext()):
            last = last.getNext()         
        return last
    
    def deleteFromFront(self):
        if self.__head is not None:
            nextHead = self.__head.getNext()
            nextHead.setPrev(None)
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
        node: Node = self.getItemByTraversal(position)
        if node and node == self.__head:
            self.__head == None
        elif node:
            # since the no reference points to object of delete node VM python delete it
            node.getPrev().setNext(node.getNext())
            if node.getNext(): node.getNext().setPrev(node.getPrev())
    
    def deleteFromEnd(self):
        if self.__head is not None:
            last = self.findLast()
            # check next available for head
            if last:
                last.getPrev().setNext(None)
                

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
                if currentNode.getNext(): 
                    currentNode = currentNode.getNext()
                else:
                    return None
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
            

    
    def printList(self, detailedPrint= False):
        currentNode = self.__head
        if currentNode:
            while(currentNode.getNext()):
                if detailedPrint:
                    print(['Node', currentNode.getData(), 'Next Node', currentNode.getNext().getData() if currentNode.getNext() else 'None', 'Prev Node', currentNode.getPrev().getData() if currentNode.getPrev() else 'None' ], ':')
                else:
                    print(currentNode.getData())
                    
                currentNode = currentNode.getNext()
            if detailedPrint:
                print(['Node', currentNode.getData(), 'Next Node', currentNode.getNext().getData() if currentNode.getNext() else 'None', 'Prev Node', currentNode.getPrev().getData() if currentNode.getPrev() else 'None' ], ':')
            else:
                print(currentNode.getData())
        
# Testing 
linkedList = DoubleLinkedListFactory()
linkedList.insertFromFront(14)
linkedList.insertFromFront(43)
linkedList.insertFromFront('IVAN')
print('-----New List------')
linkedList.printList()
linkedList.printList(True)
linkedList.insertEnd('Tom')
linkedList.insertAfter(9000, linkedList.getItemByTraversal(item=43))
print('-----New List------')
linkedList.printList()
linkedList.printList(True)
item: TraversalItem = TraversalItem(data=43)
linkedList.deleteFromMiddle(item)
print('-----New List------')
linkedList.printList()
linkedList.printList(True)
item: TraversalItem = TraversalItem(data=14)
linkedList.deleteFromMiddle(item)
item: TraversalItem = TraversalItem(data=9000)
linkedList.deleteFromMiddle(item)
print('-----New List------')
linkedList.printList()

linkedList.bubbleSortLinkedList()
print('-----Sorted List------')
linkedList.printList()