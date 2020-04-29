# Best Tiem to Buy and Sell Stock II

[link](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/)

## Description

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

## Example 1

```
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
```

## Example 2

```
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
```

## Example 3

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

## Constraints

- `1 <= prices.length <= 3 * 10 ^ 4`
- `0 <= prices[i] <= 10 ^ 4`

## Solution

### C++

[code](https://github.com/swha0901/LeetCode/blob/master/Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II/best_time_to_buy_and_sell_stock_II.cpp)

I began with initializing the variables I need for this problem.
I would need to save `maxProfit`, which is what we return, a flag to check if the transaction is on since we can only have a single transaction at a single time, the length of the prices array since I would need that multiple times, and the `boughtPrice`, well obviously.

I loop around the array a single time. In the loop I first check whether the transaction is on, to determine whether I should buy or sell. If it is on, then I first check if the index is the end of the array. At this point, I should sell since I already have a stock, and there is no more prices to look for. Otherwise, I check if the next price is lower than or equal to my current price. Then, I sell and mark transaction off since current price is the best price I can get.

If the transaction is off, if current index is not the end of the array, I check if the next price is greater than the current price. Then, since the current price is the lowest I can get, I buy and mark transaction as on.

At the end, I return the `maxProfit` which is the maximum profit I can get.
