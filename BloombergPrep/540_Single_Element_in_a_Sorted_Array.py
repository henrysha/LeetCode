"""
540. Single Element in a Sorted Array
Medium

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle - 1] != nums[middle] and nums[middle] != nums[middle + 1]:
                return nums[middle]

            left_count = middle - left

            if left_count % 2 == 1:
                if nums[middle - 1] == nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if nums[middle + 1] == nums[middle]:
                    left = middle
                else:
                    right = middle - 1

        return nums[right]


                
