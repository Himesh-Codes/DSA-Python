"""
Minimum sum partition

Given an array arr of size N containing non-negative integers, 
the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums 
is minimum and find the minimum difference.

Example 1:

Input: N = 4, arr[] = {1, 6, 11, 5} 
Output: 1
Explanation: 
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11

Solution
--------------
It is a 01 Knapsack problem basically.

DP tabulation 2D array is build with 0 ...... totalsum as x coordinate (x) and y coordinate (j) 0....each element in array.
0 element in set and 0 sum is true.
And if no element is picked up in each array iteration sum is 0.
And the 0 elements picked cannot produce other sums.

"""

class MinSumOfArrayPartition():
    
    def minSumDifference(self, arr):
        totalSum = sum(arr)
        dp = [[False for item in range(totalSum+1)] for index in range(len(arr)+1)]
        # 0 element is picked up is 0 sum.
        dp[0][0] = True
        
        # And if no element is picked up in each array iteration sum is 0. Here j index is sum.
        for index in range(len(arr)+1):
            dp[index][0] = True
        
        # And the 0 elements picked cannot produce other sums.
        for sumIndex in range(1,totalSum+1):
            dp[0][sumIndex] = False
        
        for index in range(1,len(arr)+1):
            for sumIndex in range(1,totalSum+1):
                # previous element sum includes in current
                dp[index][sumIndex] = dp[index-1][sumIndex]
                
                 # If i'th element is included
                if arr[index - 1] <= sumIndex:
                    dp[index][sumIndex] |= dp[index - 1][sumIndex - arr[index - 1]]
                    
            
        diff = float('inf')
 
        # Find the largest j such that dp[n][j]
        # is true where j loops from sum/2 t0 0
        for j in range(totalSum // 2, -1, -1):
            # from the half of the sum iterating reverse we will find what is maximum 
            # s2 = sum -s1, so diff = s2 -s1, ie, diff = sum -s1 -s1, diff = sum - 2s1
            if dp[len(arr)][j] == True:
                diff = totalSum - (2 * j)
                break
    
        return diff
            
            
# testing
arr = [3,2,7]
min = MinSumOfArrayPartition()
print(min.minSumDifference(arr))