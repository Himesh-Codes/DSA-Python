"""
Binary search tree is a data structure that quickly allows us to maintain a sorted list of numbers.

It is called a binary tree because each tree node has a maximum of two children.
It is called a search tree because it can be used to search for the presence of a number in O(log(n)) time.
- All nodes of left subtree are less than the root node
- All nodes of right subtree are more than the root node
- Both subtrees of each node are also BSTs i.e. they have the above two properties

Complexity
--------------------
 	        Worst case	Average Case
Search	        O(n)	    O(log(n))
Insert	        O(1)	    O(log(n))
Deletion	    O(1)	    O(log(n))

Space Complexity : O(n)
"""

from ast import Delete


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree(object):
    def __init__(self, root):
        self.__root = root
        
    def createNode(self, data):
        return Node(data)
    
    def deleteNodeFromRoot(self, data):
        self.deleteNode(self.__root, data)
        
    def insertFromRoot(self, data):
        if self.__root is None:
            self.__root = self.createNode(data)
        self.insertNode(self.__root, data)
        
    def insertNode(self, node: Node, data):
        if node is None:
            return self.createNode(data)
        elif data < node.data:
            node.left = self.insertNode(node.left, data)
        elif data > node.data:
            node.right = self.insertNode(node.right, data)
        return node
    
    def searchItemFromRoot(self, data):
        self.searchItem(self.__root, data)
        
    def searchItem(self, node: Node, data):
        if node is None:
            return None
        elif data < node.data:
            return self.searchItem(node.left, data)
        elif data > node.data:
            return self.searchItem(node.right, data)
        elif data == node.data:
            return node
        
    def getMininumValueFromNodes(self, node: Node):
        currentNode = node
        while currentNode.left is None:
            currentNode = currentNode.left
        return currentNode
        
    def deleteNode(self, node: Node, data):
        # if tree empty
        if node is None:
            return node
        # find the node
        if data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else:
            # either one child or no child
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            else:
            # if both child exist
                temp = self.getMininumValueFromNodes(node.right)
                node.data = temp.data
                node.right = self.deleteNode(node.right, temp.data)
        return node
    
    
    def preOrder(self):
        self.__preOrderTraversal(self.__root)
    
    def __preOrderTraversal(self, node: Node):
        if node:
            print(f'{str(node.data)} ->', end='')
            self.__preOrderTraversal(node.left)
            self.__preOrderTraversal(node.right)
            
    def inOrder(self):
        self.__inOrderTraversal(self.__root)
    
    def __inOrderTraversal(self, node: Node, info='Root'):
        if node:
            self.__inOrderTraversal(node.left, f'L of {node.data}')
            print(f'{str(node.data)}({info}) ->', end='')
            self.__inOrderTraversal(node.right, f'R of {node.data}')
    
# Testing
binaryTree = BinarySearchTree(None)
binaryTree.insertFromRoot(13)
binaryTree.insertFromRoot(9)
binaryTree.insertFromRoot(15)
binaryTree.insertFromRoot(7)
binaryTree.insertFromRoot(5)
binaryTree.insertFromRoot(35)


print('Pre Order')
binaryTree.preOrder()

print('\nIn Order')
binaryTree.inOrder()
binaryTree.insertFromRoot(6)

print('\nIn Order')
binaryTree.inOrder()
binaryTree.deleteNodeFromRoot(7)

print('\nIn Order')
binaryTree.inOrder()