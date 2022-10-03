"""
Coin Change

Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum, 
find the number of ways you can make sum by using different combinations from coins[ ].  
Note: Assume that you have an infinite supply of each type of coin. 

Example 1:

Input:
sum = 4 , 
N = 3
coins[] = {1,2,3}
Output: 4
Explanation: Four Possible ways are:
{1,1,1,1},{1,1,2},{2,2},{1,3}.

Solution 
--------
1) We can use recursion , with for (item...in.. arr)
2) Memorization (DP Tabulation)
    Use DP array..
    -   DP array x (sum) = 0, 1 .... sum
    -   y (coin) = coins[] items
    - We create array sum * coin
    Edge cases
    ----------
    1. If the sum == coinitem get chance is equal to, chance = 1
    2. If upper coin with same sum have value then chance = chance + dp[i-1][j]
    3. If sum != coin and sum - coin have value greater than zero,  chance = chance + dp[i][sum-coin]
  
    
    
"""
class Solution:
    @staticmethod
    def count(coins, N, sum):
        # sum in y and coins in x
        dp = [[0]* (sum+1) for index in range(len(coins))]
        # since the chance for coins to generate sum 0 is a 1
        for index in range(len(coins)):
            dp[index][0] = 1
        
        for coinIndex in range(len(coins)):
            for sumItem in range(1, sum+1):
                chance = 0
                if sumItem == coins[coinIndex]: chance += 1
                elif sumItem - coins[coinIndex] > 0: chance = chance + dp[coinIndex][sumItem-coins[coinIndex]]
                # if upper coin is having some value
                if coinIndex - 1 > -1: chance += dp[coinIndex-1][sumItem]
                dp[coinIndex][sumItem] = chance
        return dp[len(coins)-1][sum]

# Testing
print(Solution.count([1,2,3], 3, 4))
print(Solution.count([1,2,5], 3, 11))