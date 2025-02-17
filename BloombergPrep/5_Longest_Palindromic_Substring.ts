/**
 * 5. Longest Palindromic Substring
 * Medium
 *
 * Given a string s, return the longest 
 * palindromic
 *  
 * substring
 *  in s.
 * 
 *  
 * 
 * Example 1:
 * 
 * Input: s = "babad"
 * Output: "bab"
 * Explanation: "aba" is also a valid answer.
 * Example 2:
 * 
 * Input: s = "cbbd"
 * Output: "bb"
 *  
 * 
 * Constraints:
 * 
 * - 1 <= s.length <= 1000
 * - s consist of only digits and English letters.
 */

function longestPalindrome(s: string): string {
    function findPalindrome(i: number, j: number): string {
        let start = i
        let end = j

        while (start >= 0 && end < s.length && s[start] == s[end]) {
            start--;
            end++;
        }
        return s.slice(start + 1, end)
    }

    let answer = ''
    for (let i = 0; i < s.length; i++) {
        const odd = findPalindrome(i, i);
        if (odd.length > answer.length) {
            answer = odd
        }

        const even = findPalindrome(i, i + 1);
        if (even.length > answer.length) {
            answer = even
        }
    }

    return answer
};
