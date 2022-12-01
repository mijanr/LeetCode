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
        result = []
        for i in range(len(nums)):
            lst = nums[:i] + nums[i+1:]
            result.append(reduce(lambda x, y: x*y, lst))
        return result
if __name__ == "__main__":
    import doctest
    doctest.testmod()