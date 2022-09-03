"""
Permutations of a given string

Given a string S. 
The task is to print all unique permutations of the given string in lexicographically sorted order.

Example 1:

Input: ABC
Output:
ABC ACB BAC BCA CAB CBA
Explanation:
Given string ABC has permutations in 6 
forms as ABC, ACB, BAC, BCA, CAB and CBA 

Array Solution
----------------

consider string as array
Edge case
----------
If array string is only one letter, return [[A]]
Else pop first element as idle and get combinations of subarray using recursion
Iterate first loop in n times len(arr)
"""


class Solution:
    def find_permutation(self, S):
        # sort string first
        S = ''.join(sorted(S))
        self.array = list(S)
        self.notVisited: list =  self.array.copy()
        self.notVisited.pop(0)
        self.notVisited.sort()
        string = [item for item in self.getPermutations(S).split(' ') if item != '']
        result = []
        # purge redudant array element
        for index in range(len(string)):
            if string[index] not in result:
                result.append(string[index])
        return result 

    def checkAndAssign(self, string: str, idleItem):
        if len(string) + 1 == len(self.array) and len(self.notVisited) > 0:
            nextIdle = self.notVisited.pop(0)
            nextIdleIndex = string.find(nextIdle)
            string = string[:nextIdleIndex] + string[nextIdleIndex+1:]
            string = idleItem + string
            string = ''.join(sorted(string))
            string = nextIdle + string
        else:
            string = string + idleItem
        return string
        
    def getPermutations(self, string):
        result = ""
        if len(string) == 1:
            return string
        for iter in range(len(string)):
            
            idleItem = string[0]
            string = string[1:]
            permutations = self.getPermutations(string)
            for permutation in permutations.split(' '):
                if permutation != '':
                    permutation = idleItem + permutation + " "
                    result += permutation
            # inorder to swap idle item and next unvisit item, and sort subrray 
            string = self.checkAndAssign(string, idleItem)
        return result


class ArraySolution:
    def find_permutation(self, S):
        self.array = list(S)
        self.notVisited: list =  self.array.copy()
        self.notVisited.pop(0)
        self.notVisited.sort()
        perms = self.getPermutations(self.array.copy())
        arrangements = ''
        for combination in perms:
           arrangements += ''.join(combination) + ' '
        return arrangements
    
    def checkAndAssign(self, array: list, idleItem):
        array.append(idleItem)
        if len(array) == len(self.array) and len(self.notVisited) > 0:
            nextIdle = self.notVisited.pop(0)
            array.pop(array.index(nextIdle))
            array.sort()
            array.insert(0, nextIdle)
        
    def getPermutations(self, array):
        result = []
        if len(array) == 1:
            return [array.copy()]
        for iter in range(len(array)):
            
            idleItem = array.pop(0)
            permutations = self.getPermutations(array)
            for permutation in permutations:
                permutation.insert(0, idleItem)
            result.extend(permutations)
            # inorder to swap idle item and next unvisit item, and sort subrray 
            self.checkAndAssign(array, idleItem)
        return result

# Testing
string = 'ABC'
sol = Solution()
print(sol.find_permutation(string))

# string = 'ABC'
# sol = ArraySolution()
# print(sol.find_permutation(string))
