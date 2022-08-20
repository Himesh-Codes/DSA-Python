"""
Array permutation using backtracking with recursion
- [1,2] taken, we insert the first element in last position to shuffle in each iteration, here [1,2] -> [2,1]
- Since we have two elements we run loop 2 times, so N items, will have N times loop.
- On each iteration first element is poped and make idle, get the permutations recursively
- If only one item in array we return [[array]], here [[2]] in first iteration, and we loop for all permutations
- And insert the idle element poped, in first position, here [[1,2]], [[2,1]] in second iteration.
- Atlast the poped item placed at last of array.
"""
        
from typing import List

class Permutation:
    def __init__(self):
        self.__notVisited = None
        self.__currentArray = None
        
    def permutation(self, array: list) -> List[List[int]]:
        self.__currentArray  = array.copy()
        self.__notVisited  = array.copy()
        self.__notVisited.pop(0)
        return self.getPermutation(array)
    
    def checkAndAssign(self, array: list, itemIndex, idleItem):
        array.append(idleItem)
        if len(array) == len(self.__currentArray) and itemIndex+1 < len(self.__currentArray):
           currentFirst = self.__notVisited.pop(0)
           array.pop(array.index(currentFirst))
           array.sort()
           array.insert(0, currentFirst)
        
    def getPermutation(self, array: list) -> List[List[int]]:
        resultantArray = []
        if (len(array) == 1):
            return [array.copy()];
        for item in range(0, len(array)):
            idleItem = array.pop(0)
            permutations = self.getPermutation(array)
            
            for permutation in permutations:
                permutation.insert(0, idleItem)
            resultantArray.extend(permutations)
            # array.append(idleItem), instead swap the positions with next iteration value
            self.checkAndAssign(array, item, idleItem);
        return resultantArray

# Testing
testArray = [1, 2, 3, 4]
perm = Permutation()
print(perm.permutation(testArray))