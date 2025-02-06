"""
1726. Tuple with Same Product
Medium

Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

 

Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 

Constraints:

- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^4
- All elements in nums are distinct.
"""

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Brute Force
        # count = 0

        # for i in range(len(nums)):
        #     seen = set([i])
        #     for j in range(len(nums)):
        #         if j in seen:
        #             continue
        #         seen.add(j)
        #         for k in range(len(nums)):
        #             if k in seen:
        #                 continue
        #             seen.add(k)
        #             for l in range(len(nums)):
        #                 if l in seen:
        #                     continue
        #                 if nums[i] * nums[j] == nums[k] * nums[l]:
        #                     count += 1
        #             seen.remove(k)
        #         seen.remove(j)

        # return count

        # product frequency with hashmap
        products = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                products[nums[i] * nums[j]] += 1

        count = 0
        for product_freq in products.values():
            count += 8 * ((product_freq - 1) * product_freq) // 2
        
        return count

