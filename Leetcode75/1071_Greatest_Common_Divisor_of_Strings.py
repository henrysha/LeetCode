"""
1071. Greatest Common Divisor of Strings
Solved
Easy

Topics

Companies

Hint
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of English uppercase letters.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # edge case: no common gcd
        if str1[0] != str2[0]:
            return ''
        

        for i in range(min(len(str1) + 1, len(str2) + 1), 0, -1):
            if len(str1) % i != 0 or len(str2) % i != 0:
                continue
            prefix = str1[:i]
            
            s1 = prefix * (len(str1) // i)
            s2 = prefix * (len(str2) // i)

            if s1 == str1 and s2 == str2:
                return prefix
        
        return ''