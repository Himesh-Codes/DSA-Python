"""
Circular Double Linked List Factory : Each node stores the data and the address of the next and previous node
Last and Head nodes are connected each other

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
    
class CircularDoubleLinkedListFactory():
    def __init__(self):
        self.__last: Node = None
        
    def insertFromFront(self, data):
        newNode = Node(data)
       
        if self.__last is not None:
            newNode.setNext(self.__last.getNext())
            newNode.setPrev(self.__last)
            self.__last.setNext(newNode)
        else:
           self.__last = newNode
           self.__last.setNext(self.__last)
           self.__last.setPrev(self.__last)
        
    def insertAfter(self, data, previousNode: Node):
        if isinstance(previousNode, Node):
            newNode = Node(data)
            if previousNode == self.__last:
                newNode.setNext(self.__last.getNext())
                self.__last.setNext(newNode)
                newNode.setPrev(self.__last)
                self.__last = newNode
            elif self.__last is None:
                self.__last = newNode
            else:
                newNode.setNext(previousNode.getNext())
                newNode.setPrev(previousNode)
                previousNode.getNext().setPrev(newNode)
                previousNode.setNext(newNode)
                
        else:
            return TypeError('Not a type of class node.')
        
    def insertEnd(self, data):
        newNode = Node(data)

        if self.__last == None:
            self.__last = newNode
        else:
            newNode.setNext(self.__last.getNext())
            self.__last.setNext(newNode)
            newNode.setPrev(self.__last)
            self.__last = newNode
            
    def findLast(self):
        last = self.__last       
        return last
    
    def deleteFromFront(self):
        if self.__last is not None:
            if self.__last == self.__last.getNext():
                self.__last = None
            else:
                nextHead = self.__last.getNext().getNext()
                nextHead.setPrev(self.__last)
                self.__last.setNext(nextHead)
        
    # custom data class type in python
    def deleteFromMiddle(self, item: TraversalItem):
        if self.__last == None:
            return
        node: Node
        position: int
        if item.data:
            position = self.getItemByTraversal(None, item.data, True)
        elif item.position:
            position = item.position
        
        # get node
        node: Node = self.getItemByTraversal(position)
        if node and node == self.__last:
            if not self.__last.getNext():
                self.__last = None 
            else:
                self.__last.getNext().setPrev(self.__last.getPrev())
                self.__last.getPrev().setNext(self.__last.getNext())
                self.__last = self.__last.getPrev()
        elif node:
            # since the no reference points to object of delete node VM python delete it
            node.getPrev().setNext(node.getNext())
            if node.getNext(): node.getNext().setPrev(node.getPrev())
    
    def deleteFromEnd(self):
        if self.__last is not None:
            if not self.__last.getNext():
                self.__last = None 
            else:
                self.__last.getNext().setPrev(self.__last.getPrev())
                self.__last.getPrev().setNext(self.__last.getNext())
                self.__last = self.__last.getPrev()
                

    # multiple type annotation - Union
    def getItemByTraversal(self, position=None, item=None, getPosition: bool=False) -> Union[Node,int]:
        currentNode = self.__last
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
        currentNode = self.__last
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
        currentNode = self.__last
        if currentNode and currentNode.getNext():
            currentNode = currentNode.getNext()
            while(currentNode.getNext() != self.__last):
                if detailedPrint:
                    print(['Node', currentNode.getData(), 'Next Node', currentNode.getNext().getData() if currentNode.getNext() else 'None', 'Prev Node', currentNode.getPrev().getData() if currentNode.getPrev() else 'None' ], ':')
                else:
                    print(currentNode.getData())
                    
                currentNode = currentNode.getNext()
            if detailedPrint:
                print(['Node', currentNode.getData(), 'Next Node', currentNode.getNext().getData() if currentNode.getNext() else 'None', 'Prev Node', currentNode.getPrev().getData() if currentNode.getPrev() else 'None' ], ':')
                print(['Node', self.__last.getData(), 'Next Node', self.__last.getNext().getData() if self.__last.getNext() else 'None', 'Prev Node', self.__last.getPrev().getData() if self.__last.getPrev() else 'None' ], ':')
            else:
                print(currentNode.getData())
                print(self.__last.getData())
        
# Testing 
linkedList = CircularDoubleLinkedListFactory()
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
linkedList.deleteFromEnd()
linkedList.deleteFromMiddle(TraversalItem(data=14))
linkedList.deleteFromFront()
print('-----New List------')
linkedList.printList()
linkedList.printList(True)
