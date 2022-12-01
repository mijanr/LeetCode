"""
Author: Md Mijanur Rahman
Date: 01/12/2022
Difficulty: Easy
Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Problem Description: You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        >>> Solution().maxProfit([7,1,5,3,6,4])
        5
        >>> Solution().maxProfit([7,6,4,3,1])
        0
        '''
        current_profit = 0
        current_lowest = prices[0]
        for price in prices:
            if price<current_lowest:
                current_lowest=price
            if current_profit < (price-current_lowest):
                current_profit = price-current_lowest
        return current_profit
if __name__ == "__main__":
    import doctest
    doctest.testmod()