# Two Sum
[link](https://leetcode.com/problems/two-sum/description/)

Description
---
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example
---
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

Solution
---
#### Python 3
[code](https://github.com/swha0901/LeetCode/blob/master/two-sum/twosum.py)

I used a dictionary containing lists of indexes to store the number's location. Reason for choosing this structure is because there maybe a duplicate number in the input array. Key to the dictionary is the number, and values stored in the list are the indexes.

While looping through the input array, I push the index into the corresponding list in the dictionary. Then, I look for the complement (i.e. target - number) in the dictionary. If complement exists, I check if the complement is at the same location of the number. If so, continue the search. Otherwise, return the index of complement and the number. 

Index of the complement is basically the first index stored in the dictionary of that number. This is because if the numbers forming the sum are the same, there will be two numbers in the array, and the first two will form the answer.

#### C
[code](https://github.com/swha0901/LeetCode/blob/master/two-sum/twosum.c)

I basically brute forced through the array using nested for loop. Reason for this is because C is faster than python, and it was bothersome to implement the Hashmap/Dictionary in C.
