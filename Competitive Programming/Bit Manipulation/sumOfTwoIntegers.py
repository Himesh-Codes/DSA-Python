"""
Sum of Two Integers
 Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:

Input: a = 1, b = 2
Output: 3

Solution 
-----------
1. We use a bit manipulation technique.
Integers have fixed length (32 bits) in java. So carry (or b) will eventually be moved out of boundary and go to 0, 
and you can get out of the while loop. This is NOT the case for the Python! Python allows unlimited length of integers. 
2. By setting up a mask 0xFFFFFFFF. & this mask with an (very long) integer will only keep the last 32 bits.

    a & 0xFFFFFFFF , sum & 0xFFFFFFFF, carry & 0xFFFFFFFF
    
eg: 2 = 1 0 and 1 = 0 1,
1) so we do XOR of, sum is 1 0 ^ 0 1 = 1 1, and to check is there a carry 
2) we check logical and left shift to add carry,  (1 0 &  0 1 ) << 1 = 0 0, 
3) while carry is 0 we do step 1 and step 2 again 
4) If sum is negative (python treat as a big number) we should complement the value after logical and with mask.
"""
class Solution:
    @staticmethod
    def getSum(a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a = a & mask
        while b!= 0:
            sum = (a^b) & mask
            carry = ((a&b) << 1)  & mask
            a = sum
            b = carry
        if (a>>31) & 1:
            return ~(a^mask)
        return a
    
# Testing
print(Solution.getSum(2, 4));
print(Solution.getSum(-12, -8));