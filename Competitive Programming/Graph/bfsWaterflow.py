class Solution:
    def solve(self, A):
        def bfs(curr):
            visited = set()
            while curr:
                temp = []
                for i, j in curr:
                    if (i, j) in visited: continue
                    visited.add((i, j))

                    colors[i][j] += 1
                    for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        # not exceeds buffer
                        if not (0 <= ii < m and 0 <= jj < n): continue
                        if A[i][j] <= A[ii][jj]: 
                            temp.append((ii, jj))
                # append the next adjacent items in cur queue
                curr = temp
            
            return
        
        m, n = len(A), len(A[0]) # dims of matrix
        # stores the count of lakes it can reach
        colors = [[0]*n for _ in range(m)]

        # stores the sources for the BFS, first col, first row
        curr = []
        for i in range(m): curr.append((i, 0))
        for j in range(n): curr.append((0, j))
        # runs the BFS
        bfs(curr)

        # similarly
        curr = []
        for i in range(m): curr.append((i, n-1))
        for j in range(n): curr.append((m-1, j))
        bfs(curr)

        # count the number of cells in colors that touch 2 lakes
        ans = 0
        for i in range(m):
            for j in range(n):
                if colors[i][j] == 2:
                    ans += 1 
        return ans
    
# Testing
heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]
waterflow = Solution()
print(waterflow.solve(heights))