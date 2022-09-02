"""
Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.

Sort an array of 0s, 1s and 2s
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

Solution
Keep index of zero, largeFirst Index as index of first 2
Insert 1 before first 2 index else append at end
Insert zero at start
"""
class Solution():
    @staticmethod
    def sort012(arr):
        result = []
        zeroIndex = 0
        oneArray = []
        twoIndex = None
        for item in arr:
            # if 2 found take the element index
            if item == 2:
                result.append(item)
                if twoIndex is None: 
                    twoIndex = len(result) - 1
            elif item == 1:
                oneArray.append(item)
            else:
                result.insert(zeroIndex,item)
                if twoIndex is not None: twoIndex += 1
        result = result[:twoIndex] + oneArray + result[twoIndex:]
        return result
    
    @staticmethod
    def spaceSort012(arr):
        def swap(array, x, y):
            array[x], array[y] =  array[y], array[x]
        
        low, mid, high = 0
        

# Testing 
arr = [0,2,1,2,0]
print(Solution.sort012(arr))