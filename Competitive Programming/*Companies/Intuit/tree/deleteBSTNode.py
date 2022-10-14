"""
Delete a node from BST

Given a Binary Search Tree and a node value X. Delete the node with the given value X from the BST. 
If no node with value x exists, then do not make any change. 

Example 1:

Input:
      2
    /   \
   1     3
X = 12
Output: 1 2 3
Explanation: In the given input there
is no node with value 12 , so the tree
will remain same.

Example 2:

Input:
            1
             \
              2
                \
                 8 
               /    \
              5      11
            /  \    /  \
           4    7  9   12
X = 9
Output: 1 2 4 5 7 8 11 12
Explanation: In the given input tree after
deleting 9 will be
             1
              \
               2
                 \
                  8
                 /   \
                5     11
               /  \     \
              4    7     12

Solution
------------------
If the BST node is found and have both right and left child. We traverse connect the node.left to its parent and traverse
at the most right end of node.left and place atmostRightNode.right as node.right.
Edge cases:
- No node found then return None.
- If only node.left, we can place node as node.left.
- If only node.right, we can place node as node.right.
- If both node.right and node.left, then go through the solutions.

"""

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Solution:
    def assignNodeHelper(self, root: Node):
        if root.left == None and root.right == None:
            return None
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            rightChild = root.right
            leftChildAtmostRight = self.findRightMost(root.left)
            leftChildAtmostRight.right = rightChild
            return root.left
    
    def findRightMost(self, node: Node):
        while(node.right is not None):
            node = node.right
        return node
    
    def deleteNode(self, root, key):
        if not root:
            return None
        if root.data == key:
            return self.assignNodeHelper(root)
        treeHead = root
        while root != None:
            if root.data > key:
                if root.left and root.left.data == key:
                    root.left = self.assignNodeHelper(root.left)
                    break;
                else:
                    root = root.left
            else:
                if root.right and root.right.data == key:
                    root.right = self.assignNodeHelper(root.right)
                    break;
                else:
                    root = root.right
        return treeHead
                
    def inOrderTraversal(self, node: Node, info='Root'):
            if node:
                self.inOrderTraversal(node.left, f'L of {node.data}')
                print(f'{str(node.data)}({info}) ->', end='')
                self.inOrderTraversal(node.right, f'R of {node.data}')
                
# Testing 
node = Node(1)
node.right = Node(2)
node.right.right = Node(8)
node.right.right.right = Node(11)
node.right.right.right.right = Node(12)
node.right.right.left = Node(5)
node.right.right.left.right = Node(7)
node.right.right.left.left = Node(4)
sol = Solution()
sol.inOrderTraversal(node)
sol.deleteNode(node,8)
print("", end="\n")
sol.inOrderTraversal(node)