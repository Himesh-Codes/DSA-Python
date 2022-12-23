"""
Given an  element array of integers, , and an integer, , determine the maximum value of the sum of any of 
its subarrays modulo .

Example


The following table lists all subarrays and their moduli:

		sum	%2
[1]		1	1
[2]		2	0
[3]		3	1
[1,2]	3	1
[2,3]	5	1
[1,2,3]	6	0
The maximum modulus is 1.

Solution
-----------
First Find prefix sum of modulo of each index.
ie, 1,2 -> 1, 1,2,3-> 0 so Prefix[3] = 0

Then we can find the all prefixSum subarray sum using two loop O(n2)
maxSum = prefix[i], and we check on the every possible subarray
maxsum = max(maxsum, (prefix[i]-prefix[j]+M) % M))
Note: m is added to make sum positive, since m%m is 0 it is not a problem to add, since give same result


"""


class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,m):
        prefixSum = {}
        currentSum = 0
        for index, item in enumerate(arr):
            currentSum = ((item%m)+currentSum) % m
            prefixSum[index] = currentSum

        maxSum = 0
        for index in range(0, len(arr)):
            maxSum = max(maxSum, prefixSum[index])
            # we strip the subarray from the left
            if index-1 > 0:
                for indexj in range(index-1, -1, -1):
                    maxSum = max(maxSum, (prefixSum[index]-prefixSum[indexj]+m)%m)
        return maxSum
                
# Testing
arr = [1,2,3]  
sol = Solution()
print(sol.maxSubArraySum(arr,2))