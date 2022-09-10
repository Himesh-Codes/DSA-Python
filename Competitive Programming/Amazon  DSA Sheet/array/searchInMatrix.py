"""
Search in a matrix
Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing order,
and a number X is given. The task is to find whether element X is present in the matrix or not.

Example 2:
arr = [[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
x= 37
Output: 1
Since we have the element

Solution
------------------
Edge case:
- Traverse in each row, find the element in between the range arr[index][0] <= ele <= arr[index][cols]
- Take the index and iterate on row to search item.
- Complexity :  O(n2)

Solution O(n)
----------------
Two pointer solution
Since last elemnt in each array row is greater in the row and first element in lowest
Column is sorted and row is sorted
So we check every first element and increment rowIndex is lesser, and reduce colIndex if greater
Edge Case
- rowIndex = 0, colIndex = n
- loop until rowIndex == n or colIndex == 0
- 
"""
class Solution:
    
    def matSearch(self,mat, N, M, X):
        rows = len(mat)
        cols = M - 1
        findrows = []
        for index in range(rows):
            if mat[index][0] <= X <= mat[index][cols]:
                findrows.append(index)
        
        for row in findrows:
            for index in range(len(mat[row])):
                if mat[row][index] == X:
                    return 1
        return 0
    
    def matOptimSearch(self,mat, N, M, X):
            rowIndex = 0
            colIndex = M - 1
            
            while rowIndex < N and colIndex < M:
                if mat[rowIndex][colIndex] == X:
                    return 1
                elif mat[rowIndex][colIndex] > X:
                    colIndex -= 1
                else:
                    rowIndex += 1
            return 0 
# testing
arr = [[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
sol = Solution()
print(sol.matOptimSearch(arr, 4, 4, 37))