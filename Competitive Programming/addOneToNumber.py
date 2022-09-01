"""
Add One To Number
Problem Description

Given a non-negative number represented as an array of digits, add 1 to the number 
( increment the number represented by the digits ).

Q : Can the input have 0's before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0's before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.
You are given a sequence of points and the order in which you need to cover the points.. 
Give the minimum number of steps in which you can achieve it. 
You start from the first point.

Example Input
Input 1:

[1, 2, 3]


Example Output
Output 1:

[1, 2, 4]

Explanation 1:

Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.
 
APPROACH SOLUTION
-----------------
Edge Cases
[5,9,9,9,9] -> [6,0,0,0,0]
[9,9,9,9,9] -> [1,0,0,0,0,0]
[0, 0, 4, 4, 6, 0] -> [4,4,6,1]
[9]
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    @staticmethod
    def plusOne(A:list):
        if len(A) == 1:
            # if 9 in first position
            if  A[0] == 9:
                A[0] = 1
                A.append(0)
            else:
                A[0] =  A[0] + 1
        else:
            # Check first trailing digit is zero
            while Solution.removeTrailingZero(A, 0) != True:
               Solution.removeTrailingZero(A, 0)
            if A[len(A) - 1] == 9:
                index =  len(A) - 1
                while index > -1:
                    if A[index] == 9:
                        # if first index is replaced by one
                        if index == 0:
                            A[index] = 1 
                            A.append(0)
                        else:
                            A[index] = 0
                    if index-1 != -1 and A[index-1] != 9:
                        A[index-1] += 1
                        break
                    index -= 1
            else:       
                A[len(A) - 1] =  A[len(A) - 1] + 1
        return A
    
    def removeTrailingZero(A, index):
        if A[index] == 0: 
                A.pop(0)
        return A[0] != 0

#Testing
arr = [9]
print(Solution.plusOne(arr))