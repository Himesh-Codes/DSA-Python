"""
Kadane's algorthim
Sliding window approach
-------------------
In which a pointer in start and end is incresed as per condition
Edge case:
- If the sum before adding each (positive number) element is a negative value sum then only total sum reduced.
- So we discard the negative and make sum = 0, before add positive number.
- On each iteration check first the sum is less than zero and we have a positive number on this iteration.
- If negative number array item greater than, negative sum we have, we make sum = 0 before adding.
Steps:
1. max_sum_so_far, max_sum_here, start, end, shiftindex
We iterate the array 
find the sum, and check if the current number is positive and the sum is negative then we make the sum = 0
Then we add the element value with item, to find new sum
Since negative number makes the sum reduced we ignore and shift  start index.
"""


class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        maxSum = -float("inf")
        currentSum = 0
        for item in arr:
            # if item is greater than zero then current sum will be larger with current item
            # to deal with negative sum, check current item greater than previous sum
            if currentSum < 0 and (item > 0 or currentSum < item):
                currentSum = 0
            currentSum = currentSum + item
            # check if the array sum greater than previous
            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum

    #Function to find the sum of contiguous subarray without negative sum
    def maxSubArrayPositiveSum(self,arr):
        maxSum = -float("inf")
        currentSum = 0
        start = end = shiftIndex = 0
        for index in range(len(arr)):
            currentSum = currentSum + arr[index]
            if currentSum < 0:
                currentSum = 0
                # shift the index to current index + 1
                shiftIndex = index + 1
            if currentSum > maxSum:
                maxSum = currentSum
                start = shiftIndex
                end = index
        return maxSum , arr[start:end]
                
# Testing
arr = [-2,1,-3,4,2,-5]  
sol = Solution()
print(sol.maxSubArraySum(arr))