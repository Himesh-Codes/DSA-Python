"""
Minimum steps to reach target by a Knight

Given a square chessboard of N x N size, the position of Knight and position of a target is given,
the task is to find out the minimum steps a Knight will take to reach the target position.

Solution
---------
Use the BFS with distance to find the minimum shortest path.
We have a visted map array and queue with cell([x,y], distance) for easy calculations.
The source node is vistited always and in queue
Edge Cases
------------
1.while queue < 1, continue
2.if currentx == targetx and currenty == targety return distance
"""

class cell():
        def __init__(self, coordinate, distance):
            self.coordinate = coordinate
            self.distance = distance

class Solution:
            
    def isValid(self, visited, x, y, N):
        if x < 1 or y < 1 or x > N or y > N or visited[x][y]:
            return False
        return True
    
    # BFS implementaion with recursion
    def minStepsForKnight(self,current, target, N):
        directions = [[2,-1], [2,1], [-2,-1], [-2,1], [-1,-2], [-1,2], [1,2], [1,-2]]
        tarX , tarY = target
        
        visited = [[False for indexI in range(N+1)] for indexJ in range(N+1)] 
        queue = []
        queue.append(cell(current, 0))
        visited[current[0]][current[1]] = True
        
        while len(queue) > 0:
            current = queue.pop(0)
            curX, curY = current.coordinate
            if curX == tarX and curY == tarY:
                return current.distance
            
            for dirX, dirY in directions:
                if self.isValid(visited, curX+dirX, curY+dirY, N):
                    queue.append(cell([curX+dirX, curY+dirY], current.distance+1))
                    visited[curX+dirX][curY+dirY] = True
        return -1
    
#  Testing
N = 30
knightpos = [1, 1]
targetpos = [30, 30]
sol = Solution()
# Function call
print(sol.minStepsForKnight(knightpos,
                            targetpos, N))