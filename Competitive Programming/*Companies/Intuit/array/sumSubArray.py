"""
Subarrays with sum K
    Given an unsorted array of integers, find the number of continuous subarrays having sum exactly equal to a given number k.


Example 1:

Input:
N = 5
Arr = {10 , 2, -2, -20, 10}
k = -10
Output: 3
Explaination: 
Subarrays: arr[0...3], arr[1...4], arr[3..4]
have sum exactly equal to -10.

Solutions
----------
Using Hashmap for prefix sum (visitedsumHashMap), we stores the sum of all prefix subarray, 
and will minus that each currentsum with the sum 
to check that if we can any prefix already found subarray sum to find our result sum.

Complexity: O(N)

Edge Case
------------
1. Initially the visitedsumHashmap has value 0 with count 1. (Becuase selecting empty subarray give sum 0)
2.If currentsum not in visitedsumHashmap add new , else update the value +1.
3. If currentSum - sum, difference is in visitedsumHashMap, that is we can remove that subarray with sum to produce 
the find sum. Then we can add that difference count with result (becuase diff=cursum-sum => sum=cursum-diff).
"""
class Solution:
    def findSubArraySum(self, Arr, N, k):
        visitedsumHashMap = {0: 1}
        currentSum = 0
        result = 0
        for item in Arr:
            currentSum += item
            diff = currentSum - k
            if diff in visitedsumHashMap:
                result += visitedsumHashMap[diff]

            if currentSum in visitedsumHashMap:
                visitedsumHashMap[currentSum] += 1
            else:
                visitedsumHashMap.update({currentSum: 1})
        return result

# Testing
sol = Solution()
arr = [1,-1,1,1,1,1]
print(sol.findSubArraySum(arr, len(arr), 3))
            
                