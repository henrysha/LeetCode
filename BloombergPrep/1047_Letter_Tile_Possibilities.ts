/**
 * 1079. Letter Tile Possibilities
 * Medium
 *
 * You have n  tiles, where each tile has one letter tiles[i] printed on it.
 * 
 * Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
 * 
 *  
 * 
 * Example 1:
 * 
 * Input: tiles = "AAB"
 * Output: 8
 * Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
 * Example 2:
 * 
 * Input: tiles = "AAABBC"
 * Output: 188
 * Example 3:
 * 
 * Input: tiles = "V"
 * Output: 1
 *  
 * 
 * Constraints:
 * 
 * 1 <= tiles.length <= 7
 * tiles consists of uppercase English letters.
 */
function numTilePossibilities(tiles: string): number {
    const sequences = new Set();

    function backtracking(sequence: string, visited: boolean[]) {
        if (sequence.length > 0) {
            sequences.add(sequence);
        }

        for (let i = 0; i < tiles.length; i++) {
            if (visited[i]) continue
            visited[i] = true
            backtracking(sequence + tiles[i], visited)
            visited[i] = false
        }
    }

    const visited = Array(tiles.length).fill(false)

    backtracking('', visited)

    return sequences.size
};
