"""
 Merge K Sorted Linked Lists
 
Input: k = 3, n =  4
list1 = 1->3->5->7->NULL
list2 = 2->4->6->8->NULL
list3 = 0->9->10->11->NULL

Output: 0->1->2->3->4->5->6->7->8->9->10->11
Merged lists in a sorted order 
where every element is greater.
 
Solution
-----------
Use merge sort approach by adding compare, merge and insert linkedlists untill list length is sorted into 1.
We need a condition until the every array of LinkedList is merged into one single Array.
Compare 2 LinkedList at a time. Add them to the new List, 
Repeat the merge of Lists until only single list exists.
Edge Cases
--------
1) If the list len is 0 return None
2) On mergeList if list 1 or list 2 is not fully traversed append the rest item into new LinkedList might returns as result.
Complexity
----------
O(N log k) 

"""

from typing import List


class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data

class Solution:
    def mergeKLinkedLists(self, lists: List[Node]):
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            # since 2 lists a re compared once we iterate in steps 2
            for index in range(0, len(lists), 2):
                listOne = lists[index]
                listTwo = lists[index + 1] if index + 1 < len(lists) else None
                mergedLists.append(self.mergeLinkedLists(listOne, listTwo))
            lists = mergedLists
        return lists[0]
    
    def mergeLinkedLists(self, listsOne:Node, listTwo:Node):
        resultList = Node(None)
        currentNode = resultList
        while listsOne and listTwo:
            if listsOne.data > listTwo.data:
                currentNode.next = listTwo
                listTwo = listTwo.next
            else:
                currentNode.next = listsOne
                listsOne = listsOne.next
            currentNode = currentNode.next
        # append residual elements in any list
        if listsOne:
            currentNode.next = listsOne
        
        if listTwo:
            currentNode.next = listTwo
        return resultList.next

# Testing
one = Node(3)
one.next = Node(9)
one.next.next = Node(10)

two = Node(1)
two.next = Node(2)
two.next.next = Node(5)

three = Node(6)
three.next = Node(7)
three.next.next = Node(8)

sol = Solution()
res = sol.mergeKLinkedLists([one, two, three])
while res:
    print(res.data, "->")
    res = res.next