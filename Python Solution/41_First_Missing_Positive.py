"""
Author: Md Mijanur Rahman
Date: 03/12/2022
Difficulty: Hard
Problem Link: https://leetcode.com/problems/first-missing-positive/
Problem Description: Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
"""
import doctest
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        >>> Solution().firstMissingPositive([1,2,0])
        3
        >>> Solution().firstMissingPositive([3,4,-1,1])
        2
        >>> Solution().firstMissingPositive([7,8,9,11,12])
        1
        """
        hashSet = set(nums)
        ans = 1
        while True:
            if ans not in hashSet:
                return ans
            ans +=1 

if __name__ == "__main__":
    doctest.testmod(verbose=True)
