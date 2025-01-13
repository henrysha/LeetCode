"""
1318. Minimum Flips to Make a OR b Equal to c
Medium

Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

 

Example 1:



Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
Example 2:

Input: a = 4, b = 2, c = 7
Output: 1
Example 3:

Input: a = 1, b = 2, c = 3
Output: 0
 

Constraints:

- 1 <= a <= 10^9
- 1 <= b <= 10^9
- 1 <= c <= 10^9
"""

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # Naive Approach (faster due to minimum bitwise operation.)
        flips = 0

        while c > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if bit_a | bit_b != bit_c:
                if bit_c == 0:
                    if bit_a == 1:
                        flips += 1
                    if bit_b == 1:
                        flips += 1
                else:
                    flips += 1
            
            a = a >> 1
            b = b >> 1
            c = c >> 1
        
        while a > 0:
            bit = a & 1
            if bit == 1:
                flips += 1
            a = a >> 1
        
        while b > 0:
            bit = b & 1
            if bit == 1:
                flips += 1
            b = b >> 1
        
        return flips

        # More pythonic Approach (Slower runtime due to more bitwise operations)

        # flips = 0

        # while a or b or c:
        #     if c & 1 == 1:
        #         flips += 1 if a & 1 == 0 and b & 1 == 0 else 0
        #     else:
        #         flips += (a & 1) + (b & 1)
        #     a = a >> 1
        #     b = b >> 1
        #     c = c >> 1
        # return flip
