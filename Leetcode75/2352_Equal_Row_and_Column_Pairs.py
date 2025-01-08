"""
2352. Equal Row and Column Pairs
Medium

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

- n == grid.length == grid[i].length
- 1 <= n <= 200
- 1 <= grid[i][j] <= 10^5
"""

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Brute Force
        # count = 0

        # for i in range(n):
        #     for j in range(n):
        #         match = True
        #         for k in range(n):
        #             if grid[i][k] != grid[k][j]:
        #                 match = False
        #                 break
        #         if match:
        #             count += 1
        
        # return count

        # Hash Map Optimized

        hashmap = {}

        for i in range(n):
            s = ','.join([str(num) for num in grid[i]])
            if s not in hashmap:
                hashmap[s] = 1
            else:
                hashmap[s] += 1
        
        count = 0
        for j in range(n):
            s = ','.join([str(grid[i][j]) for i in range(n)])
            if s in hashmap:
                count += hashmap[s]
        return count

