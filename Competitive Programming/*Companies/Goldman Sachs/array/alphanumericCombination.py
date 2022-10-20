"""
Alphanumeric Combination

We will give a string, and need to find the combination of words can be formed.
1 <= number <= 25.
If zero is coming as number we should concat the zero in between with the preceding number.
Need to return the number of possible ways of combination.
Eg: 2101
possible outcome is (2) (10) (1)
Output : 1

Solution
---------
Use recursive approach with a decision tree. And push the results of combination. Then return length of result array.

Edge Case
-----------
1. On each iteration of string number, either index item or combination of index, index+1 item will be placed.
 IF AND ONLY IF the number in range of 0 < number < 26 (index, index+1 item will be placed.).
2. When combination of index, index+1 is formed we will check if index+2 is not 0.
3. On each iteration checks the index + 1 is not zero, if zero, only include the index, index+1 combination in array.
4. Append result array if len of combination index is equals total length. And if result not in result array.
5. Return the result len.
"""

class Solution:
    def checkTheAlphanumericCombinations(self, inputStr):
        result = []
        # convert into array
        inputArray = [*inputStr]
        
        def combinations(input, indexCount,  combinationStr):
            
            if indexCount == len(inputStr) and combinationStr not in result:
                result.append(combinationStr)
                return
            
            combination = combinationStr.copy()
            while input:
                number = input.pop(0)
                combination.append(number)
                indexCount +=1 
                if input:
                    if input[0] == '0': 
                        number = combination.pop()
                        number += input.pop(0)
                        combination.append(number)
                        indexCount +=1 
                        
                    combinations(input.copy(), indexCount, combination.copy())
                  
                    # we can make a combination of index , index+1
                    if len(number) < 2 and len(input) >=1:
                          # check the 3 rd element from current element is not zero. 
                          # if zero donot do a combination
                        if len(input) >=2 and input[1] == '0':
                            return
                        number = combination.pop()
                        number += input.pop(0)
                        
                        if 0 < int(number) <= 26:
                            combination.append(number)
                            indexCount +=1 
                            combinations(input.copy(), indexCount, combination.copy())
                else:
                    combinations(input.copy(), indexCount, combination.copy())

        combinations(inputArray.copy(), 0, [])
        return len(result)

# Testing
inputStr = '2910'
sol = Solution()
print(sol.checkTheAlphanumericCombinations(inputStr))
inputStr = '2112'
print(sol.checkTheAlphanumericCombinations(inputStr))
inputStr = '923014'
print(sol.checkTheAlphanumericCombinations(inputStr))