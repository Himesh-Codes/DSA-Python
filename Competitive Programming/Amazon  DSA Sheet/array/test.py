class Solution:
    # Edge case
    # Iterate through the first item of each row, 
    # if found a row start greater than element we search we search in prevoius row
    # else search in last row only
    def matSearch(self,mat, N, M, X):
        rows = len(mat)
        cols = M - 1
        findrow = rows - 1
        for index in range(rows):
            if mat[index][0] < X < mat[index][cols]:
                findrow = index
                break
        
        for index in range(len(mat[findrow])):
            if mat[findrow][index] == X:
                return 1
        return 0
    
# testing
arr = [[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
sol = Solution()
print(sol.matSearch(arr, 4, 4, 37))