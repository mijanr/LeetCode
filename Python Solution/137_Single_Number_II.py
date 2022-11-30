"""
Author: Md Mijanur Rahman
Date: 30/11/2022
Difficulty: Medium
Problem Link: https://leetcode.com/problems/single-number-ii/description/
Problem Description: Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else: 
                hashMap[num] += 1
        for key, val in hashMap.items():
            if val==1:
                return key
    
if __name__ == "__main__":
    nums_1 = [2,2,3,2] # 3
    nums_2 = [0,1,0,1,0,1,99] # 99
    solution = Solution()
    for nums in [nums_1, nums_2]:
        print(solution.singleNumber(nums))