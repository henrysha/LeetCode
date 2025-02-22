"""
347. Top K Frequent Elements
Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n log n)
        # counts = Counter(nums)

        # sorted_counts = sorted([(num, counts[num]) for num in counts], key=lambda x: x[1], reverse=True)

        # return list(map(lambda x: x[0], sorted_counts[:k]))

        # O(n log k) heap solution
        counts = Counter(nums)

        heap = []

        for num in counts:
            heapq.heappush(heap, (-counts[num], num))

        ans = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            ans.append(num)
        
        return ans
