# Remove Duplicates from Sorted Array
[link](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/)

Description
---
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1
---
```
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
```

Example 2
---
```
Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
```

Solution
---
#### C++
[code](https://github.com/swha0901/LeetCode/blob/master/Remove%20Duplicates%20from%20Sorted%20Array/remove_dup_from_sorted_array.cpp)

I began with a null check to prevent null pointer error to the array.

Since the array is already sorted, I saved two integers : current number and the index to put in the next number.
Then, as I iterated through the array, I compared the current number to the integer in the array. If the current number is smaller, I substitute the number at the saved index to the number at current iteration. Then, I save the number and increment the index.

The index saved is essentially equal to the size of non-duplicate array, so I return the index saved.