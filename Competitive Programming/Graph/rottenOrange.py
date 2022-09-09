"""
Rotten Oranges
Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the minimum time required to rot all oranges. 
A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] 
(up, down, left and right) in unit time. 

Example 1:

Input: grid = {{0,1,2},{0,1,2},{2,1,1}}
Output: 1
Explanation: The grid is-
0 1 2
0 1 2
2 1 1
Oranges at positions (0,2), (1,2), (2,0)
will rot oranges at (0,1), (1,1), (2,2) and 
(2,1) in unit time.

Solution
--------------
Find fresh oranges count, rotten oranges coordinates as queue
Do a BFS , with while loop until fresh count == 0 or no rotten oranges are to be visted.
time is incremented on every while loop.
On each iteration of quue items the new discovered rotten oranges will be added to queue.

Complexity
------------
n = number of rows
m = number of cols 
O(n*m)
"""

from collections import deque
from typing import List

class RottenOrange():
    def getAllRottenOranges(self, orangeStack: List[List[int]]):
        rottenDeck = deque()
        freshCount, time = 0,0

        ROWS, COLS = len(orangeStack), len(orangeStack[0])
        # find the rotten coordinatees appended to the queue, fresh oranges number
        for row in range(ROWS):
            for col in range(COLS):
                if orangeStack[row][col] == 1:
                    freshCount += 1
                elif orangeStack[row][col] == 2:
                    rottenDeck.append([row, col])
            
        # edge case is no fresh oranges
        # and no items on the rotten deck
        while freshCount > 0 and rottenDeck:
            # doing a BFS on the rotten orange items
            for iteration in range(len(rottenDeck)):
                rRow, rCol = rottenDeck.popleft()
                # direction of rotting
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                for drow, dcol in directions:
                    row, col = rRow + drow, rCol + dcol
                    # check edge case of boundary, and item is fresh, we skip this iteration
                    if row < 0 or row == ROWS or col < 0 or col == COLS or orangeStack[row][col] != 1:
                        continue
                    # append new rotten to rotten deque, make the rack rotten
                    orangeStack[row][col] = 2
                    rottenDeck.append([row,col])
                    freshCount -= 1
            time += 1
        return time if freshCount == 0 else -1
    
# Testing
array = [[0,1,2],[0,1,2],[2,1,1]]
rotten  = RottenOrange()
print(rotten.getAllRottenOranges(array))
grid = [[2,2,0,1]]
print(rotten.getAllRottenOranges(grid))
grid = [[2,1,1,1,2,1,2,0,2],
[1,2,1,1,2,1,1,2,2],
[2,2,1,2,2,1,1,2,1],
[1,0,2,0,1,2,2,1,0],
[2,0,0,2,2,2,2,0,2],
[2,1,1,1,2,0,2,1,2],
[2,2,1,1,0,0,1,2,2],
[0,2,0,2,2,2,2,2,1],
[2,0,2,0,1,2,2,2,2],
[1,1,1,2,0,1,2,2,2]]
print(rotten.getAllRottenOranges(grid))