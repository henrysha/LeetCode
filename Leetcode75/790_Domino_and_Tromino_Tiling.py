"""
790. Domino and Tromino Tiling
Medium

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

Example 1:


Input: n = 3
Output: 5
Explanation: The five different ways are show above.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

- 1 <= n <= 1000
"""

class Solution:
    def numTilings(self, n: int) -> int:
        # Implementation from Some Clever Dude in discussion
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2

        # dp = [1] * (n+1)

        # dp[2] = 2

        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] * 2 + dp[i-3]

        # return dp[n] % (pow(10,9) + 7)

        # DP Approach
        # Case 1: add vertical domino to right of N-1 Board
        # Case 2: add 2 horizontal dominos to the right of N-2 Board
        # Case 3: add tromino to partially covered N-1 Board (one tile is not covered)
        #         we can find symmetric case for Case 3

        # Base case
        # n == 1 -> 1, n == 2 -> 2
        # if n <= 2:
        #     return n
        
        # f = [0] * n
        # f[0] = 1
        # f[1] = 2

        # p = [0] * n
        # p[1] = 1

        # for i in range(2, n):
        #     f[i] = f[i-1] + f[i-2] + 2 * p[i-1]
        #     p[i] = p[i-1] + f[i-2]
        
        # return f[-1] % 1_000_000_007

        # DP Space Optimal
        # To calculate f[i] / p[i] in the above DP, we need three variables
        # -> f[i-1] / f[i-2] / p[i-1]
        # -> f_curr / f_prev / p_curr
        # when progressing the curr pointer, we can update f_curr to be
        # f_curr + f_prev + 2 * p_curr
        # and p_curr to be
        # p_curr + f_prev
        # we can update f_prev to be the f_curr before progression.

        # Base case
        # n == 1 -> 1, n == 2 -> 2
        if n <= 2:
            return n

        MOD = 1_000_000_007
        
        f_prev = 1
        f_curr = 2

        p_curr = 1

        for i in range(3, n+1):
            tmp = f_curr
            f_curr = (f_curr + f_prev + 2 * p_curr) % MOD
            p_curr = (p_curr + f_prev) % MOD
            f_prev = tmp
        
        return f_curr