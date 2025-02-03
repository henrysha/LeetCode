"""
200. Number of Islands
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        WATER = '0'
        LAND = '1'
        DIRECTIONS = [(1,0), (-1, 0), (0, 1), (0, -1)]

        m, n = len(grid), len(grid[0])

        island_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == WATER:
                    continue
                
                island_count += 1
                queue = deque([(i, j)])
                grid[i][j] = WATER

                while queue:
                    (row, col) = queue.popleft()
                    for (k, l) in DIRECTIONS:
                        next_i, next_j = row + k, col + l
                        if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == LAND:
                            queue.append((next_i, next_j))
                            grid[next_i][next_j] = WATER
        

        return island_count
