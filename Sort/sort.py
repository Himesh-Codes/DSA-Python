"""
1. Bubble Sort Optimised: Complexity - O(n2)
    - The array is iterated untill the count, minimimum as first and compare with next element.
    - Nextstep change minimum to second item and compare with next element.
    - For each iteration check swapped flag, if swapped flag false in any iteration stop iteration,
    since array is sorted already.
2. Selection sort: Complexity - O(n2)
    - Select the first element of each iteration (ie, 0, 1, 2, ...), as minimum, selection step item
    - Loop on unsorted elements, Compare with the next items, and select the minimum 
    - After each second loop iteration, swap the selection step item, with the minimum item index
    - Continue until loop ends
"""


class ArraySort():
    
    def __init__(self, array=None):
        self.array = array if array is not None else []
    
    # Class method used as a factory method and return the class object
    # cls calls the constructor
    # These methods can be called with the class name
    @classmethod
    def includeArray(cls, array: list):
        return cls(array)
    
    # Static items can be called from using Class name
    # In optimised bubble sort we uses swapped flag to check previous iteration made any swap
    @staticmethod
    def bubbleSort(array):
        for index in range(len(array)):
            swapped = False
            for secondIndex in range(0, len(array) - index - 1):
                if array[secondIndex] > array[secondIndex + 1]:
                    array[secondIndex], array[secondIndex + 1] = array[secondIndex + 1], array[secondIndex]
                    swapped = True
            if swapped == False:
                break
        return array
    
    # Select minimum item is found on each iteration ends, swap with the stepIndex
    # second loop always begins from next element of stepIndex
    @staticmethod
    def selectionSort(array):
        for stepIndex in range(len(array)):
            minItemId = stepIndex
            for unsortedItemIndex in range(stepIndex + 1, len(array)):
                if array[minItemId] > array[unsortedItemIndex]:
                    minItemId = unsortedItemIndex
            # putting minimum at correct position
            array[stepIndex], array[minItemId] = array[minItemId], array[stepIndex]
        return array
    
    # let first element be sorted,set second element as key and compare to left elements 
    # increase key item index and check on left side items on array
    # insert the key in correct position
    #complexity O(n2)
    @staticmethod
    def insertionSort(array: list):
        for index in range(1, len(array)):
            key = array[index]
            leftItemsIndex = index - 1
            
            while(leftItemsIndex >= 0 and key < array[leftItemsIndex]):
                array[leftItemsIndex+1] = array[leftItemsIndex]
                leftItemsIndex -= 1
            array[leftItemsIndex+1] = key
        return array
    
    #Divide and conquer rule used, split the array into two sub arrays
    #Complexity : O(n log(n))
    #The main array is placed with each element from left with comparing elements of two arrays
    #Check last any elements in any of the subarray is needed to be traversed, if then runs second loop
    @staticmethod
    def mergeSort(array):
        if len(array) > 1:
            midLength = len(array) // 2

            leftSubarray = array[:midLength]
            rightSubarray = array[midLength:]
            
            ArraySort.mergeSort(leftSubarray)
            ArraySort.mergeSort(rightSubarray)

            leftIndex = rightIndex = currentIndex = 0
            while leftIndex < len(leftSubarray) and rightIndex < len(rightSubarray):
                if leftSubarray[leftIndex] < rightSubarray[rightIndex]:
                    array[currentIndex] = leftSubarray[leftIndex]
                    leftIndex += 1
                else:
                    array[currentIndex] = rightSubarray[rightIndex]
                    rightIndex += 1
                currentIndex += 1
            
            # if left subarray have more items
            while leftIndex < len(leftSubarray):
                array[currentIndex] = leftSubarray[leftIndex]
                leftIndex += 1
                currentIndex += 1
            # if right subarray have more items
            while rightIndex < len(rightSubarray):
                array[currentIndex] = rightSubarray[rightIndex]
                rightIndex += 1
                currentIndex += 1
        return array
                
    
# Testing
testArray = [-1, 34, 6, 0, 23, 45]
print(ArraySort.bubbleSort(testArray))
testArray = [-2, -4, 7, 0, 180, 45, 87, 51, 3, 17]
print("Selection sort")
print(ArraySort.selectionSort(testArray))
testArray1 = [-2, -4, 7, 0, 180, 45, 87, 51, 3, 17]
print("Insertion sort")
print(ArraySort.insertionSort(testArray1))
testArray2 = [-2, -4, 7, 0, 180, 45, 87, 51, 3, 17]
print(testArray2)
print("Merge sort")
print(ArraySort.mergeSort(testArray2))