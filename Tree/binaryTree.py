"""
Binary Tree
A collection of disjoint trees is called a forest.

Types of tree
--------------------
1. Full Binary Tree: A full Binary tree is a special type of binary tree in 
    which every parent node/internal node has either two or no children.
    
2. Perfect Binary Tree: A perfect binary tree is a type of binary tree in which every internal node 
    has exactly two child nodes and all the leaf nodes are at the same level.

3. Complete Binary Tree: 
    Every level must be completely filled
    All the leaf elements must lean towards the left.
    The last leaf element might not have a right sibling i.e. 
    a complete binary tree doesn't have to be a full binary tree.

4. Degenerate or Pathological Tree: A degenerate or pathological tree is the tree 
    having a single child either left or right.
    
5. Skewed Binary Tree:
    A skewed binary tree is a pathological/degenerate tree in which the tree is either dominated by the 
    left nodes or the right nodes. 
    Thus, there are two types of skewed binary tree: left-skewed binary tree and right-skewed binary tree.

6. Balanced Binary Tree:
    It is a type of binary tree in which the difference between the height of the 
    left and the right subtree for each node is either 0 or 1.
"""

from tabnanny import check
from turtle import right
from tree import TreeTraversal

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree(TreeTraversal):
    def __init__(self, root):
        super().__init__(root)
        
    # count total nodes
    def countNodes(self, node: Node):
        if node is None:
            return 0
        return 1 + (self.countNodes(node.left) + self.countNodes(node.right))
        
    # check full binary tree
    def isFullTree(self):
        return self.checkIsFullTree(self.getRoot())
    
    # check perfect binary tree
    def isPerfectTree(self):
        return self.checkIsPerfectTree(self.getRoot(), self.maxDepth(self.getRoot()))
    
     # check complete binary tree
    def isCompleteTree(self):
        return self.checkComplete(self.getRoot(), 0, self.countNodes(self.getRoot()))
    
     # check balanced binary tree
    def isBalancedTree(self):
        return self.checkBalancedBinaryTree(self.getRoot())
        
    def checkIsFullTree(self, node: Node):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return (self.checkIsFullTree(node.left) and self.checkIsFullTree(node.right))
        return False
    
    def maxDepth(self, node: Node):
        if node is None:
            return -1
        return max(self.maxDepth(node.left) , self.maxDepth(node.right)) + 1  
    
    def getHeight(self, node, height=1):
        if node is None:
            return height
        return max(self.getHeight(node.left, height+1) , self.getHeight(node.right, height+1))
    
    def checkIsPerfectTree(self, node: Node, depth, position=0):  
        if node is None:
            return True
        if node.left is None and node.right is None:
            return (depth == position+1)
        elif node.left is None or node.right is None:
            return False
        
        if node.left is not None and node.right is not None:
            return(self.checkIsPerfectTree(node.left, depth, position+1) and self.checkIsPerfectTree(node.right, depth, position+1))
            
            
    # using the property i as index, 2i + 1 is left index and 2i + 2 is right index, 
    # parent index of any elem low((i-1)/2)
    # arrange nodes in array with index as order of tree push
    def checkComplete(self, node, index, totalNodes):
        if node is None:
            return True
        elif index >= totalNodes:
            return False
        return(self.checkComplete(node.left, (2*index) + 1, totalNodes) and self.checkComplete(node.right, (2*index) + 2, totalNodes))
    
    # check with property the hieght of left - right subtree of each nodes is 1/0
    def checkBalancedBinaryTree(self, node: Node):
        if node is None:
            return True
        elif abs(self.getHeight(node.left) - self.getHeight(node.right)) <= 1:
            return True
        return False
        

tree = BinaryTree(Node(1))
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

tree.getRoot().right = two
tree.getRoot().left = three
tree.getRoot().left.left = four
tree.getRoot().left.right = five

print('Inorder Traversal')
tree.inOrder()

print('\n',tree.isFullTree())

tree.getRoot().left.right.left = Node(6)
print(tree.isFullTree())

print(tree.maxDepth(tree.getRoot()))

print("Perfect Tree Check")
print(tree.isPerfectTree())

print("Complete Tree Check")
print(tree.isCompleteTree())

print("Balanced Tree Check")
print(tree.isBalancedTree())