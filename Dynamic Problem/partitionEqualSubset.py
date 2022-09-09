"""
Partition Equal Subset Sum - Dynamic Programming 

Given a non-empty array nums containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Solution
------------
It is basically a 01 Knapsack problem.
We need a sum of direct half to be obtained to split into equal subarray, ie our target.

We keep as DP set which maintains the elements and sum of each and every combination. 
Initially DP will have 0 as only element, since sum can be zero.

We iterate through every element, and add with each element with DP.
Altast check is exist our target in set then, we can split array into two.

Edge Case
----------
If sum is odd we cannot split into equal array sum.

Example:

Input: nums = [1,5,11,5]
Output: true
Explanation: Since we have an element 11, and total sum is 22. The array can be partitioned as [1, 5, 5] and [11].
"""
class EqualSubSet():
    
    def isEquallySplittedArray(self, array):
        total = sum(array)
        # we need a sum of direct half to be obtained to split into equal subarray
        target = total // 2
        # If sum is odd we cannot split into equal array sum
        if total % 2 != 0: return False
        dp = set()
        # initially 0 wil be only sum
        dp.add(0)
        for element in array:
            # we need to make a copy of global sum dp set.
            currentDP = dp.copy()
            for sumItem in dp:
                currentDP.add(sumItem + element)
                currentDP.add(element)
            dp = currentDP
        return True if target in dp else False
        
# Testing
nums = [1,5,11,5]
subset = EqualSubSet()
print(subset.isEquallySplittedArray(nums))
        
        