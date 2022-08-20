"""
The next permutation pattern identification
Each element in array have weightage, here [1,2,3,4], weightage as 4:1, 3:2, 2:3, 1:4..
From first element excluded, We find the rigthmost highest peak element (with low weightage), 
and swap with immediate left.
- Case 1: If right left cannot be found then the array is descending array, so we sort and give 
least ascending array. Here, [1,2,3,4] is least asecding array.
- Case 2: If we found a highest element, and found other highest element in between the current highest element
and its immedeiate left, eg: 1,2,3,5,4 -> 1,2,4,3,5 is next highest permutation, so we will find 3,5 first, then
we find 4 that is in btw 3,5. 
After swapped the elements, the right elements are sorted ascending inorder to get next permutation,
ie, here 3 & 4 swapped 1,2,4,5,3 -> 1,2,4,3,5 sorted to get next order.
"""
class NextPermutation:
    
    def nextPermutation(self, array: list):
        # Identify edge case , if one element
        if len(array) == 1:
            return array
        
        # exclude the first element in 0 index
        index = 1
        peakElementIndex = -1
        while(index<len(array)):
            if array[index] > array[index-1]:
                peakElementIndex = index
            index += 1
            
        # if no peak element then array is at its max descending order
        #sort array ascending and return
        if peakElementIndex == -1:
            array.sort()
            return array
        else:
            # check next element in between current peak and its immediate left
            newPeakIndex = peakElementIndex
            for index in range(peakElementIndex+1, len(array)):
                if array[index] > array[peakElementIndex-1] and array[index] < array[newPeakIndex]:
                    newPeakIndex = index
            # swap
            array[newPeakIndex], array[peakElementIndex-1] = array[peakElementIndex-1], array[newPeakIndex]
            # sort the right elements from swapped element
            refactoredArray =  array[:peakElementIndex]
            sortArray = array[peakElementIndex:]
            sortArray.sort()
            refactoredArray.extend(sortArray)
        return refactoredArray
            
            
# Testing
solve = NextPermutation()
print(solve.nextPermutation([1,2,3,5,4]))