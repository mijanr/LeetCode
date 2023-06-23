"""
Author: Md Mijanur Rahman
Date: 30/11/2022
Difficulty: Easy
Problem Link: https://leetcode.com/problems/binary-search/
Problem Description: Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        final = len(nums)
        mid = len(nums) // 2
        keep = True
        while keep:
            if nums[mid] < target:
                first = mid
                mid = (first + final) // 2
            elif nums[mid] > target:
                final = mid
                mid = (first + final) // 2
            else:
                return mid
            if target > nums[-1] or target < nums[0]:
                keep = False
                return -1
            if target not in nums:
                return -1


if __name__ == "__main__":
    nums_1 = [-1, 0, 3, 5, 9, 12]
    target_1 = 9  # Output: 4
    nums_2 = [-1, 0, 3, 5, 9, 12]
    target_2 = 2  # Output: -1
    solution = Solution()
    print(solution.search(nums_1, target_1))
    print(solution.search(nums_2, target_2))
