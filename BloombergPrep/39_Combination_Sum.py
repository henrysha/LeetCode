"""
39. Combination Sum
Medium

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct.
- 1 <= target <= 40
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # DP (Very Inefficient)
        # if target < 2:
        #     return []

        # dp = [[] for _ in range(target + 1)]

        # for i in range(2, target + 1):
        #     counts = []
        #     for candidate in candidates:
        #         prev = i - candidate
        #         if prev > 0:
        #             for prevNode in dp[prev]:
        #                 count = Counter(prevNode)
        #                 count[candidate] += 1
        #                 if count in counts:
        #                     continue
        #                 dp[i].append(prevNode + [candidate])
        #                 counts.append(count)
        #     if i in candidates:
        #         dp[i].append([i])
        # return dp[-1]

        # Backtracking

        if target < 2:
            return []

        ans = []

        def backtracking(remainder: int, node: List[int], start: int):
            if remainder < 0:
                return
            if remainder == 0:
                ans.append(node)
                return

            for i in range(start, len(candidates)):
                backtracking(remainder - candidates[i], node + [candidates[i]], i)

        backtracking(target,[],0)

        return ans


