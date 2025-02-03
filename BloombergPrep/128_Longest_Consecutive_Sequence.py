"""
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        unique = set(nums)

        max_count = 1

        for num in unique:
            if num - 1 not in unique and num + 1 in unique:
                curr = num
                count = 0
                while curr in unique:
                    count += 1
                    curr += 1
                if count > max_count:
                    max_count = count
        
        return max_count
