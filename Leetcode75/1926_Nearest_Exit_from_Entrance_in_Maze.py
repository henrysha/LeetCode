"""
1926. Nearest Exit from Entrance in Maze
Medium

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

 

Example 1:


Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
Example 2:


Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
Example 3:


Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
 

Constraints:

- maze.length == m
- maze[i].length == n
- 1 <= m, n <= 100
- maze[i][j] is either '.' or '+'.
- entrance.length == 2
- 0 <= entrance_row < m
- 0 <= entrance_col < n
- entrance will always be an empty cell.
"""

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right

        width, height = len(maze[0]), len(maze)

        queue = deque([(entrance[1], entrance[0], 0)])
        maze[entrance[0]][entrance[1]] = '+'

        while queue:
            x, y, path = queue.popleft()

            for (j, i) in DIRECTIONS:
                next_x, next_y = x + i, y + j

                if next_x < 0 or next_y < 0 or next_x >= width or next_y >= height or maze[next_y][next_x] == '+':
                    continue

                if next_x == 0 or next_y == 0 or next_x == width - 1 or next_y == height - 1:
                    return path + 1

                maze[next_y][next_x] = '+'
                queue.append((next_x, next_y, path + 1))

        return -1
