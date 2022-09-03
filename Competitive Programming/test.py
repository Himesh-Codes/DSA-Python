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