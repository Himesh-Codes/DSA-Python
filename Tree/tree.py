"""
 In order to perform any operation in a linear data structure, the time complexity increases with the 
 increase in the data size. But, it is not acceptable in today's computational world.

Node
A node is an entity that contains a key or value and pointers to its child nodes.

Edge
It is the link between any two nodes.

Root
It is the topmost node of a tree.

Height of a Node
The height of a node is the number of edges from the node to the deepest leaf.

Depth of node
The depth of a node is the number of edges from the root to the node.

Degree of a Node
The degree of a node is the total number of branches of that node.

Forest
A collection of disjoint trees is called a forest.

Types of tree
--------------------
Binary tree
Binary search tree
AVL tree
B-tree

Tree traversal
--------------------
(L -left subtrees, N- Root, R-right subtrees)
Inorder - L N R
Preorder - N L R
Postorder - L R N

Applications
--------------------
Binary Search Trees(BSTs) are used to quickly check whether an element is present in a set or not.
Heap is a kind of tree that is used for heap sort.
A modified version of a tree called Tries is used in modern routers to store routing information.
Most popular databases use B-Trees and T-Trees, which are variants of the tree structure we learned 
above to store their data.
Compilers use a syntax tree to validate the syntax of every program you write.
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TreeTraversal():
    def __init__(self, root: Node):
        self.__root = root
        
    def addLeft(self, parent: Node, node: Node):
        parent.left = node
        
    def addRight(self, parent: Node, node: Node):
        parent.right = node

    def getRoot(self):
        return self.__root;
    
    def inOrder(self):
        self.__inOrderTraversal(self.__root)
    
    def preOrder(self):
        self.__preOrderTraversal(self.__root)
    
    def postOrder(self):
        self.__postOrderTraversal(self.__root)
        
    def __inOrderTraversal(self, node: Node):
        if node:
            self.__inOrderTraversal(node.left)
            print(f'{str(node.data)} ->', end='')
            self.__inOrderTraversal(node.right)
            
    def __preOrderTraversal(self, node: Node):
        if node:
            print(f'{str(node.data)} ->', end='')
            self.__preOrderTraversal(node.left)
            self.__preOrderTraversal(node.right)
            
    def __postOrderTraversal(self, node: Node):
        if node:
            self.__postOrderTraversal(node.left)
            self.__postOrderTraversal(node.right)
            print(f'{str(node.data)} ->', end='')
            
# Testing
tree = TreeTraversal(Node(1))
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
print('Preorder Traversal')
tree.preOrder()
print('Postorder Traversal')
tree.postOrder()