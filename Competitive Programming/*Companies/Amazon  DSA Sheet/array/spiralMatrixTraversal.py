"""
Spirally traversing a matrix

Given a matrix of size r*c. Traverse the matrix in spiral form.

Example 1:

Input:
r = 4, c = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15,16}}
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Solution
----------
Pointer based problem.
We will traverse the matrix in single go.
So, Complexity is O(n*m).
We will maintain, left = 0, top =0, right = cols, bottom = rows.

Edge Cases
----------
We run while left < right and top < bottom.
1) for left .. right, increase top++ . (since top level is traversed)
2) for top .. bottom, decrease right-- . (since right level is traversed)
3) for right... left, -1, decrease bottom-- . (since bottom level is traversed)
4) for bottom ... top, -1, increase left++. (since top left is traversed)
"""

class Solution:
    
    def spirallyTraverse(self,matrix, r, c): 
        traverse = []
        left, top = 0, 0
        right = c
        bottom = r
        
        while left < right and top < bottom:
            
            # get values from left to right 
            for index in range(left, right):
                traverse.append(matrix[top][index])
            top += 1
                
            # get values from top to bottom 
            for index in range(top, bottom):
                traverse.append(matrix[index][right-1])
            right -= 1
            
            # we need to check if left<right or top < bottom
            if not(left < right and top < bottom):
                break
                 
            # get values from right to left, in descending order 
            for index in range(right-1, left-1, -1):
                traverse.append(matrix[bottom-1][index])
            bottom -= 1
                 
            # get values from bottom to top, in descending order 
            for index in range(bottom-1, top-1, -1):
                traverse.append(matrix[index][left])
            left += 1
        return traverse
    
# Testing
r = 4
c = 4
matrix = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15,16]]

sol = Solution()
# print(sol.spirallyTraverse(matrix, r, c))

r= 2 
c= 3
matrix = [[5,11,30],
[5,19,19]]
print(sol.spirallyTraverse(matrix, r, c))