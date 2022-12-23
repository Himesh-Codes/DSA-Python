"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
Secondary
-----------
To remove the cycle in the loop use same two pointer (slow/fast) method.

1 - 2 - 3 - 4 -5 -6 -7 -8-9-10-6
He we take count of element is loop, and place 1st point in head 2nd on {count} element.
On iteration check 2nd.next == 1st, then first is head and second is last of loop.
"""


class Node():
      def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
            
def detectCycle(head: Node):
    firstPointer = secondPointer = head
    while (firstPointer and secondPointer and secondPointer.next):
        firstPointer = firstPointer.next
        secondPointer = secondPointer.next.next
        if (secondPointer == firstPointer):
            removeLoop(secondPointer,head)
            return 1
    return 0

def removeLoop(node, head):
    firstPointer = node
    secondPointer = node.next
    count = 1
    while (secondPointer != firstPointer):
        count += 1
        secondPointer = secondPointer.next
    # second pointer placed in the count number position  from head, so that we can iterate equally
    secondPointer = head
    firstPointer = head
    while(count > 1):
        secondPointer = secondPointer.next
        count -= 1
    # we can see on iteration if 2nd.next == 1st then 2nd is last
    while(secondPointer.next != firstPointer):
        secondPointer = secondPointer.next
        firstPointer = firstPointer.next
    secondPointer.next = None
        
            
def printList(node):
    while(node):
        print(node.data, '->', end=" ")
        node = node.next
    
# TESTING
node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)
node.next.next.next.next.next = node.next.next

print(detectCycle(node))
printList(node)