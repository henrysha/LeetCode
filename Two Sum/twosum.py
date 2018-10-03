class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers = {}
        for i in range(len(nums)):
            if nums[i] not in numbers:
                numbers[nums[i]] = []
            numbers[nums[i]].append(i)
            complement = target-nums[i]
            if complement in numbers:
                if numbers[complement][0] == i:
                    continue
                return [numbers[complement][0],i]