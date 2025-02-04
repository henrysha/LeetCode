"""
9. Palindrome Number
Easy

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

- -2^31 <= x <= 2^31 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert int to string
        # s = str(x)
        # left, right = 0, len(s) - 1

        # while left < right:
        #     if s[left] != s[right]:
        #         return False
        #     left += 1
        #     right -= 1

        # return True

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        curr = x
        revertedNumber = 0

        while curr > 0:
            revertedNumber = revertedNumber * 10 + curr % 10
            curr //= 10
        
        return x == revertedNumber

