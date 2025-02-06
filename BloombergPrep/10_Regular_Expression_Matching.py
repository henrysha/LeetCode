"""
10. Regular Expression Matching
Hard

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

- 1 <= s.length <= 20
- 1 <= p.length <= 20
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '*'.
- It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # recursive
        # if not p:
        #     return not s
        
        # first_match = bool(s) and p[0] in {s[0], '.'}

        # if len(p) >= 2 and p[1] == '*':
        #     return (
        #         self.isMatch(s, p[2:])
        #         or first_match
        #         and self.isMatch(s[1:], p)
        #     )
        # else:
        #     return first_match and self.isMatch(s[1:], p[1:])

        # DP

        dp = [[False] * (len(p) + 1) for _ in range((len(s) + 1))]

        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        
        return dp[0][0]

