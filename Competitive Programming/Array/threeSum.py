"""
Three Sum
The array is given , and a sum is given , so three numbers in array may be add to give a sum.
Eg Input:
[2,4,7,9,13,15,21,42]
sum=37

Output:
3,4,5

Solution:
Rather than doing a hashing technique of 2 loops, two pointer technique from first to last index
Sort array
Loop in array range index

from its leftIndex -1 and rightIndex +1, do loop
and find the sum elements
Increment leftIndex if sum > total, else rightIndex decrement

Complexity: O(N*2)
"""
class ThreeSum():
    @staticmethod
    # use generator function to find all combinations
    def twoPointSolution(array: list, sum):
        tempArray = array.copy()
        tempArray.sort()
        for index in range(len(tempArray)):
            # the two pointers start on left = index + 1 and right = len(arr) + 1
            leftIndex = index + 1
            rightIndex = len(tempArray) - 1
            while (leftIndex<rightIndex and leftIndex > 0 and rightIndex < len(tempArray)):
                total = array[leftIndex] + array[index] + array[rightIndex]
                if total == sum:
                    yield array.index(array[index]), array.index(array[leftIndex]), array.index(array[rightIndex])
                    leftIndex += 1
                    rightIndex -= 1
                elif total<sum:
                    leftIndex += 1
                else:
                    rightIndex -= 1
        return 0,0,0

arr = [2,4,6,7,9,10,12,15,21,42]
sum = 37
for points in ThreeSum.twoPointSolution(arr, sum):
    print(points)
