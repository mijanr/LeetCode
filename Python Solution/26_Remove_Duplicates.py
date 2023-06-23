"""
Author: Md Mijanur Rahman
Date: 22/06/2023
Difficulty: Easy
Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
Problem Description: Given a sorted array nums, remove the duplicates in-place such that each element appears 
                    only once and returns the new length. Do not allocate extra space for another array, 
                    you must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List
import doctest


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        >>> Solution().removeDuplicates([1,1,2])
        2
        >>> Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
        5
        """
        if not nums:
            return 0
        i = 1
        for idx in range(len(nums) - 1):
            if nums[idx] != nums[idx + 1]:
                i += 1
        return i


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    # print(Solution().removeDuplicates([1,1,2]))
