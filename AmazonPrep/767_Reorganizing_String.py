"""
767. Reorganize String
Medium

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

- 1 <= s.length <= 500
- s consists of lowercase English letters.
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Heap solution
        # counts = Counter(s)

        # heap = []

        # for c, count in counts.items():
        #     heapq.heappush(heap, (-count, c))
        
        # ans = []

        # while heap:
        #     neg_count, c = heapq.heappop(heap)
        #     if not ans or ans[-1] != c:
        #         neg_count += 1
        #         ans.append(c)
        #         if neg_count != 0:
        #             heapq.heappush(heap, (neg_count, c))
        #         continue
            
        #     if not heap:
        #         return ""
            
        #     next_count, next_c = heapq.heappop(heap)
            
        #     ans.append(next_c)
        #     next_count += 1
        #     if next_count != 0:
        #         heapq.heappush(heap, (next_count, next_c))
            
        #     heapq.heappush(heap, (neg_count, c))
        
        # return ''.join(ans)

        # Counter + Odd / Even Solution

        counts = Counter(s)

        max_count, max_letter = 0, ''

        for c, count in counts.items():
            if count > max_count:
                max_count = count
                max_letter = c

        if max_count > (len(s) + 1) // 2:
            return ''
        
        ans = [''] * len(s)

        index = 0
        for i in range(max_count):
            ans[index] = max_letter
            index += 2
            counts[max_letter] -= 1
        
        for c, count in counts.items():
            if count == 0:
                continue
            for _ in range(count):
                if index >= len(s):
                    index = 1
                ans[index] = c
                index += 2
            
        return ''.join(ans)

