"""
79. Word Search
Medium

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

class Solution:
    DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

    def findWord(self, board: List[List[str]], word: str, startPos: (int, int)) -> bool:
        seen = [[False] * len(board[0]) for _ in range(len(board))]
        seen[startPos[0]][startPos[1]] = True

        def backtracking(row, col, i):
            if i == len(word) - 1:
                return True

            for (r, c) in self.DIRECTIONS:
                next_row = row + r
                next_col = col + c
                if not (0 <= next_row < len(board)) \
                        or not (0 <= next_col < len(board[0])):
                    continue
                if seen[next_row][next_col]:
                    continue
                if board[next_row][next_col] == word[i + 1]:
                    seen[next_row][next_col] = True
                    if backtracking(next_row, next_col, i + 1):
                        return True
                    seen[next_row][next_col] = False
                        
            return False
        
        return backtracking(startPos[0], startPos[1], 0)

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    if self.findWord(board, word, (i, j)):
                        return True
        return False


