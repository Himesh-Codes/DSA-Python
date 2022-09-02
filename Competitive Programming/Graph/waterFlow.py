"""
Water Flow
Problem Description

Given an N x M matrix A of non-negative integers representing the height of each unit cell in a continent,
the "Blue lake" touches the left and top edges of the matrix and the "Red lake" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) 
from a cell to another one with height equal or lower.

Output:
Find the number of cells from where water can flow to both the Blue and Red lake.

Example Input
Input 1:

 A = [
       [1, 2, 2, 3, 5]
       [3, 2, 3, 4, 4]
       [2, 4, 5, 3, 1]
       [6, 7, 1, 4, 5]
       [5, 1, 1, 2, 4]
     ]
     
Example Output
Output 1:

 7
 
Solution:
The Pacific (blue) and Atlantic (red), we find the all cells reach from the each blue and red ocean .
Store each cell coordinate in which connected to pacific & atlantic oceans.
Do a DFS from each border cells in atlantic/pacific.

Edge Cases:
In DFS
row < 0 & col < 0, row> ROWLEN & col > COLLEN, 
coordinate not visited in atalantic and pacific set, height is lesser than prevoius height in flow area.
then return.

Finally get the intersection of sets in pacific & atlantic 

Complexity
-----------
O(M*N)

"""


class WaterFlow():
    def __init__(self, flowAreaMatrix):
       self.__flowArea = flowAreaMatrix
    
    def getWaterFlows(self):
        def isValid(row, col, visitOcean, previousHieght):
             # If the cell already present is visited ocean list
            # current height is lesser than prevoius height in flow area
            if row < 0 or col < 0 or row == ROWLEN or col == COLLEN or (row,col) in visitOcean or self.__flowArea[row][col] < previousHieght:
                return False
            return True
        
        def dfs(row, col, visitOcean: set, previousHieght):
            if isValid(row, col, visitOcean, previousHieght) is not True:
               return
            # if it reaches any cell it reaches pacific or atlantic ocean for sure
            visitOcean.add((row,col))
            # do iterative DFS to left,right,top,down
            dfs(row, col-1, visitOcean, self.__flowArea[row][col])
            dfs(row, col+1, visitOcean, self.__flowArea[row][col])
            dfs(row-1, col, visitOcean, self.__flowArea[row][col])
            dfs(row+1, col, visitOcean, self.__flowArea[row][col])
                
        # The Row length and column lenght is finded, arr[0] len give columns length
        ROWLEN, COLLEN = len(self.__flowArea), len(self.__flowArea[0])
        pacific, atlantic = set(), set()
        
        # I need to traverse on first row & last row
        # Do a DFS
        for COL in range(COLLEN):
            # first row is pacific ocean, hieght as current first col
            dfs(0, COL, pacific, self.__flowArea[0][COL])
            #last row is atlantic ocean
            dfs(ROWLEN-1, COL, atlantic, self.__flowArea[ROWLEN-1][COL])
        
        # I need to traverse on first column & last col
        # Do a DFS
        for ROW in range(ROWLEN):
            # first col is pacific ocean
            dfs(ROW, 0, pacific, self.__flowArea[ROW][0])
            #last col is atlantic ocean
            dfs(ROW, COLLEN-1, atlantic, self.__flowArea[ROW][COLLEN-1])
        
        intersectOceanPoints = pacific.intersection(atlantic)
        return len(intersectOceanPoints)

# Testing
heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]
waterflow = WaterFlow(heights)
print(waterflow.getWaterFlows())
heights = [
    [2,2],
    [2,2]
]
waterflow = WaterFlow(heights)
print(waterflow.getWaterFlows())