"""
Author: Md Mijanur Rahman
Date: 16/11/2023
Difficulty: Easy
Problem Link: https://leetcode.com/problems/missing-number/
Problem Description: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        >>> Solution().missingNumber([3,0,1])
        2
        >>> Solution().missingNumber([0,1])
        2
        >>> Solution().missingNumber([9,6,4,2,3,5,7,0,1])
        8
        >>> Solution().missingNumber([0])
        1
        """
        n = len(nums)
        return int((n * (n + 1)) / 2 - sum(nums))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
