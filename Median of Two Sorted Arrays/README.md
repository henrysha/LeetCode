# Median of Two Sorted Arrays
[LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)

There are two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively.

Find the median of the two sorted arrays. The overall run time complexity should be `O(log (m+n))`.

You may assume `nums1` and `nums2` cannot be both empty.

### Example 1 :

```ruby
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

### Example 2 :

```ruby
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

## Solution
Concatenate `nums1` and `nums2` and sort the arrays.

Find the index of the median by dividing the `length-1` by 2.

If index is Integer, return the median. If not, get the indexes around the calculated index, and get the average.

[Solution](median_of_two_sorted_arrays.rb)
```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Float}
def find_median_sorted_arrays(nums1, nums2)
    merged_nums = (nums1+nums2).sort!
    median_index = (merged_nums.length-1)/2.to_f
    if median_index.floor == median_index
        merged_nums[median_index.to_i].to_f
    else
        (merged_nums[(median_index-0.5).to_i] + merged_nums[(median_index+0.5).to_i])/2.to_f
    end
end
```