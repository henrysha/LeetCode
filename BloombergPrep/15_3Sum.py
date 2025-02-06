"""
15. 3Sum
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # hashmap + hashset
        # ans, dups = set(), set()

        # seen = {}

        # for i in range(len(nums)):
        #     if nums[i] in dups:
        #         continue
        #     dups.add(nums[i])
        #     for j in range(i + 1, len(nums)):
        #         complement = -nums[i] - nums[j]

        #         if complement in seen and seen[complement] == i:
        #             ans.add(tuple(sorted((nums[i], complement, nums[j]))))
        #         else:
        #             seen[nums[j]] = i


        # return list(ans)

        # sort + two pointer

        ans = []

        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]

            left, right = i + 1, len(nums) - 1

            while left < right:
                x = nums[left] + nums[right]
                if x == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif x < target:
                    left += 1
                else:
                    right -= 1 
                
        return ans
