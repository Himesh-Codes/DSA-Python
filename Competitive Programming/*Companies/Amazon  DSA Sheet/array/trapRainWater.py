"""
Trapping Rain Water

Given an array arr[] of N non-negative integers representing the height of blocks. 
If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

Input:
N = 6
arr[] = {3,0,0,2,0,4}
Output:
10

Input:
N = 4
arr[] = {7,4,0,9}
Output:
10
Explanation:
Water trapped by above 
block of height 4 is 3 units and above 
block of height 0 is 7 units. So, the 
total unit of water trapped is 10 units.

Solution
------------
1) Using multiple arrays
   O(N) space complexity, we find, maxleft[], maxRight[], min(maxLeft, maxRight) [], and waterTrap []

2) Using two pointer left, right, maxLeft, maxRight is found dynamically
    we run until left < right
    increement left if leftmax < rightMax, find max left, and use formulae water = min(maxleft, maxright) - arr[left]
    else incremetn right, find max right
"""


class Solution:
    def trappingWater(self, arr,n):
        left, right = 0, n - 1 
        waterUnits = 0
        maxLeft, maxRight = arr[left], arr[right]
        
        while left < right:
            
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, arr[left])
                waterContainerSize = min(maxLeft, maxRight) - arr[left] 
                waterUnits += waterContainerSize if waterContainerSize > 0 else 0
               
            else:
                right -= 1
                maxRight = max(maxRight, arr[right])
                waterContainerSize = min(maxLeft, maxRight) - arr[right]
                waterUnits += waterContainerSize if waterContainerSize > 0 else 0
             
        return waterUnits
    
# Testing
arr = [7,4,0,9]
water = Solution()
print(water.trappingWater(arr, len(arr)))