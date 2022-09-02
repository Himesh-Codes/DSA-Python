"""
Min Steps in Infinite Grid
Problem Description

You are in an infinite 2D grid where you can move in any of the 8 directions

 (x,y) to 
    (x-1, y-1), 
    (x-1, y)  , 
    (x-1, y+1), 
    (x  , y-1),
    (x  , y+1), 
    (x+1, y-1), 
    (x+1, y)  , 
    (x+1, y+1) 
You are given a sequence of points and the order in which you need to cover the points.. 
Give the minimum number of steps in which you can achieve it. 
You start from the first point.

Example Input
Input 1:

 A = [0, 1, 1]
 B = [0, 1, 2]

Example Output
Output 1:

 2

Explanation 1:

 Given three points are: (0, 0), (1, 1) and (1, 2).
 It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
 
APPROACH SOLUTION
-----------------
- Loop through array, A & B, firstItemRange as eg: A[0]-A[1], secondItemRange  B[0]-B[1]
- Use abs() to get rid of negative value and max - min approach
- Edge case if array have only 1 length, no step so return 0
- Add max steps taken in each steps by substract array values in index order
- Return steps
"""

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    @staticmethod
    def coverPoints(A, B):
        if len(A) > 1:
            steps = 0
            for index in range(0, len(A)-1):
                firstItemDiff = abs(max(A[index], A[index+1]) - min(A[index+1], A[index]))
                secondItemDiff = abs(max(B[index], B[index+1]) - min(B[index+1], B[index]))
                steps += max(firstItemDiff, secondItemDiff)
            return steps
        else:
            return 0
        
# Testing
A = [4,8,-7,-16]
B = [4,-15,-10,32]
# Expected output steps are 76
print(Solution.coverPoints(A,B))