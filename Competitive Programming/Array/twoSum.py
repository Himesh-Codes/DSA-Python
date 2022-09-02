"""
Two Sum 
The array is given and a sum is given to find the array elements with sum equal to be return its indexes
Eg:
Input 
[1,43,12,41,2,5], sum=17

Output
2,5

Solution:
Divide and conquer
---------
Sort the array
find min element , ie; sum/2
find the index of array element greater equal than half value

Visited dict
---------------
Keep a visited item and its index dictionary 
In each iteration find the difference and check in visited dict
Else not found return 0,0
"""

class TwoSum():
    
    @staticmethod
    def optimesolution(sum, array: list):
        tempArray = array.copy()
        tempArray.sort()
        halfValue = sum // 2
        minIndex = next(index for index, item in enumerate(tempArray) if item >= halfValue)
        if minIndex+1 < len(tempArray) and tempArray[minIndex+1] == halfValue:
            return minIndex, minIndex+1
        lessArray = tempArray[:minIndex]
        largeArray = tempArray[minIndex:]
        for largeitemindex in range(len(largeArray)):
            for minitemindex in range(minIndex-1, -1, -1):
                if (largeArray[largeitemindex] + lessArray[minitemindex]) == sum:
                    return array.index(lessArray[minitemindex]), array.index(largeArray[largeitemindex])
                if (largeArray[largeitemindex] + lessArray[minitemindex]) < sum:
                    break
        return 0,0
    
    @staticmethod
    def dictsolution(sum, array: list):
        visitDict = {}
        for index, item in enumerate(array):
            difference = sum - item
            if difference in visitDict:
                return visitDict[difference], index
            visitDict[item] = index
        return 0,0
            
            
        
# Testing
arr = [1,34,43,5,6,7,12,18]
sum = 30
sum2 = 16
twosum = TwoSum()
print(twosum.optimesolution(sum, arr))
print(twosum.optimesolution(sum2, arr))

print(twosum.dictsolution(sum, arr))
print(twosum.dictsolution(sum2, arr))