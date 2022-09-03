"""
Nth node from end of linked list

Given a linked list consisting of L nodes and given a number N. 
The task is to find the Nth node from the end of the linked list.

Example 1:

Input:
N = 2
LinkedList: 1->2->3->4->5->6->7->8->9
Output: 8
Explanation: In the first example, there
are 9 nodes in linked list and we need
to find 2nd node from end. 2nd node
from end os 8. 

Solution
-----------
Push items to array
Get len(arr)-n to get position of item from front.
Return -1 if pos < 0
else return arr[pos] element

"""
class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
            
def getNthFromLast(head,n):
    arr = []
    current = head
    if head.next == None:
        arr.append(head.data)
    
    while current != None:
        arr.append(current.data)
        current = current.next
    
    pos = len(arr) - n
    if pos < 0:
        return -1
    else:
        return arr[pos]

# testing
head = Node(1)
PRENEXT = Node(2)
head.next = PRENEXT
NEXT = Node(3)
PRENEXT.next = NEXT
PRENEXT = NEXT
NEXT = Node(4)
PRENEXT.next = NEXT
PRENEXT = NEXT
NEXT = Node(5)
PRENEXT.next = NEXT
PRENEXT = NEXT
NEXT = Node(6)
PRENEXT.next = NEXT
PRENEXT = NEXT
NEXT = Node(7)
PRENEXT.next = NEXT
PRENEXT = NEXT
NEXT = Node(8)
PRENEXT.next = NEXT
PRENEXT = NEXT
NEXT = Node(9)
PRENEXT.next = NEXT
PRENEXT = NEXT
print(getNthFromLast(head, 2))