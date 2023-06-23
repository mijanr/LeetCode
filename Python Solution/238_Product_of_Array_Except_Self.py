"""
Author: Md Mijanur Rahman
Date: 01/12/2022
Difficulty: Medium
Problem Link: https://leetcode.com/problems/product-of-array-except-self/
Problem Description:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
from typing import List
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        >>> Solution().productExceptSelf([1,2,3,4])
        [24, 12, 8, 6]
        >>> Solution().productExceptSelf([-1,1,0,-3,3])
        [0, 0, 9, 0, 0]
        """
        prefix = []
        suffix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[i - 1] * nums[i])
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix.append(nums[i])
            else:
                suffix.append(suffix[-1] * nums[i])
        suffix.reverse()
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(suffix[i + 1])
            elif i == len(nums) - 1:
                res.append(prefix[i - 1])
            else:
                res.append(prefix[i - 1] * suffix[i + 1])
        return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
