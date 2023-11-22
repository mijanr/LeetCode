"""
Author: Md Mijanur Rahman
Date: 22/11/2023
Difficulty: Easy
Problem Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
Problem Description: 
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""

from typing import List
import doctest

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        >>> Solution().findDifference([1,2,3], [2,4,6])
        [[1, 3], [4, 6]]
        >>> Solution().findDifference([1,2,3,3], [1,1,2,2])
        [[3], []]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        lst_1 = [num for num in nums1 if num not in nums2]
        lst_2 = [num for num in nums2 if num not in nums1]
        return [lst_1, lst_2]
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)
        