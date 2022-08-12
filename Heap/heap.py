"""
HEAP is a complete binary tree
- Max heap : always greater than its child node/s and the key of the root node 
    is the largest among all other nodes. 
- Min heap : always smaller than the child node/s and the key of the root node 
    is the smallest among all other nodes.

Heap Data Structure Applications
-----------------------------------
Heap is used while implementing a priority queue.
Dijkstra's Algorithm
Heap Sort
"""

class Heap():
    def __init__(self):
        self.array = []
        
    def heapify(self, array, totalnumber, index):
        largest = index
        # left and right child index of binary tree in an array
        left = (2 * index) + 1
        right = (2 * index) + 2
        
        if left < totalnumber and array[left] > array[index]:
            largest = left
        if right < totalnumber and array[right] > largest:
            largest = right
        if largest != index:
            array[index], array[largest] = array[largest], array[index]
            self.heapify(array, totalnumber, largest)
            
    def insertItem(self, array: list, item):
        if len(array) == 0:
            array.append(item)
        else:
            array.append(item)
            # taking the half will get the all subtrees node to be matched with its child nodes
            for index in range((len(array) // 2)- 1, -1, -1):
                self.heapify(array, len(array), index)