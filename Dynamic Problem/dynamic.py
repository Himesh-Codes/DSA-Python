"""
Dynamic Programming

If any problem can be divided into subproblems, which in turn are divided into smaller subproblems, 
and if there are overlapping among these subproblems, then the solutions to these subproblems can be saved 
for future reference. In this way, efficiency of the CPU can be enhanced. 
This method of solving a solution is referred to as dynamic programming.

Dynamic Programming Example
Let's find the fibonacci sequence upto 5th term. 
A fibonacci series is the sequence of numbers in which each number is the sum of the two preceding ones. 
For example, 0,1,1, 2, 3. Here, each number is the sum of the two preceding numbers.

Recursion vs Dynamic Programming
Dynamic programming is mostly applied to recursive algorithms. 
This is not a coincidence, most optimization problems require recursion and dynamic programming 
is used for optimization.

But not all problems that use recursion can use Dynamic Programming. 
Unless there is a presence of overlapping subproblems like in the fibonacci sequence problem, 
a recursion can only reach the solution using a divide and conquer approach.

Climbing Stairs

You are climbing a stair case and it takes A steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example :

Input 1:

A = 2 Output 1:

2 Explanation 1:

[1, 1], [2] Input 2:

A = 3 Output 2:

3 Explanation 2: 

[1 1 1], [1 2], [2 1]

Soloution
-----------
Memorization technique or tabulation technique.
We use bottom up formulae, the last / destination step output is 1.
So in bottom up loop, we found the arrangement of dp(n) step is dp(n+1) , dp(n+2).
dp[0] will give the iterative result.
"""
class Solution:
    # @param A : integer
	# @return an integer
	def climbStairs(self, A):
            dp = [0 for item in range(A+1)]
            dp[0] = 0
            dp[A] = 1
            for index in range(A-1, -1, -1):
                dp[index] = dp[index+1] + (dp[index+2] if index+2 <= A else 0)
            return dp[0]
                
# testing

sol  = Solution()
print(sol.climbStairs(2))