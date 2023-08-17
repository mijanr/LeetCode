"""
Author: Md Mijanur Rahman
Date: 22/06/2023
Difficulty: Easy
Problem Link: https://leetcode.com/problems/majority-element/
Problem Description: Given an array nums of size n, return the majority element.
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        >>> Solution().majorityElement([3,2,3])
        3
        >>> Solution().majorityElement([2,2,1,1,1,2,2])
        2
        """
        maps = {}
        for num in nums:
            if num in maps:
                maps[num] += 1
            else:
                maps[num] = 1
        maxx = {}
        for key, val in maps.items():
            pass
        pass
