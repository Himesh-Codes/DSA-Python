"""
Find the maximum number on traversal of matrix

"""
def getMatrixMaxValue(matrix):
    # Write your code here
    global maximumValue
    maximumValue = 0
    collen = len(matrix[0])
    rowlen = len(matrix)
    def isInRange(indexI, indexJ):
        if (0 <= indexI and indexI < rowlen) and (0 <= indexJ and indexJ < collen):
            return True
        return False
    
    def traverseMatrix(indexI, indexJ, currentValue):
        global maximumValue
        if not isInRange(indexI, indexJ):
            maximumValue = max(maximumValue, currentValue)
            return
        currentValue += matrix[indexI][indexJ]
        traverseMatrix(indexI, indexJ+1, currentValue)
        traverseMatrix(indexI+1, indexJ, currentValue)
       
    traverseMatrix(0,0, 0)
    return maximumValue

# Testing 
mat = [[10, 12, 20, 5], [12, 23, 43, 44], [23, 12, 43, 56]]
print(getMatrixMaxValue(mat))