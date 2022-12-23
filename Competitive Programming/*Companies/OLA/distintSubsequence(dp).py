"""
Find number of times a string occurs as a subsequence in given string

Given two strings, find the number of times the second string occurs in the first string, whether continuous or discontinuous.

Examples: 

Input:  
string a = "GeeksforGeeks"
string b = "Gks"

Output: 4

Explanation:  
The four strings are - (Check characters marked in bold)
GeeksforGeeks
GeeksforGeeks
GeeksforGeeks
GeeksforGeeks

Solution
---------
1) We will match the each string by string, 
    a) If the string matches each other we increment indexA + 1 and indexB + 1, And indexA + 1 , indexB not incremented to
        check whether the same string is presented.
    b) If not match we indexA + 1, not indexB.
2) We will be using the DP to store the matched strings count on each state/ each indexes.

Edge Cases
-------------
1. If the string a is "" (empty), and string b not empty then it is return 0.
2. If the string b is "" (empty), and string a not empty then it is return 1 becuase without selecting 
    any char we can produce "".
3. If both strings are "" (empty), we return 1.

Complexity
------------
O(N*M) - Time & Space (Since DP is used).

"""

class Solution:
    def numDistinct(self, s: str, t: str):
        cache = {}

        if (s == "" and t == "") or (s != "" and t == ""):
            return 1
        elif (s == "" and t != ""):
            return 0
        
        def dfs(indexI, indexJ):
            if indexJ == len(t):
                return 1
            if indexI == len(s):
                return 0
            if (indexI,indexJ) in cache:
                return cache[(indexI, indexJ)]
            if s[indexI] == t[indexJ]:
                cache[(indexI, indexJ)] = dfs(indexI+1, indexJ+1) + dfs(indexI+1, indexJ)
            else:
                cache[(indexI, indexJ)] = dfs(indexI+1, indexJ)
            return cache[(indexI, indexJ)]
        
        return dfs(0,0)
    
# Testing
sol = Solution()
print(sol.numDistinct("rabbbit", "rabbit"))