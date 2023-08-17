"""
Author: Md Mijanur Rahman
Date: 30/11/2022
Difficulty: Medium
Problem Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Problem Description: Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""
from typing import List
import doctest


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        >>>Solution().twoSum([2,7,11,15], 9)
        [1, 2]
        >>>Solution().twoSum([2,3,4], 6)
        [1, 3]
        >>>Solution().twoSum([-1,0], -1)
        [1, 2]

        """
        hashMap = {}
        for idx, num in enumerate(numbers):
            if num not in hashMap:
                hashMap[target - num] = idx + 1
            else:
                return [hashMap[num], idx + 1]
        return []


if __name__ == "__main__":
    """
    numbers_1 = [2, 7, 11, 15]
    target_1 = 9  # [1,2]
    numbers_2 = [2, 3, 4]
    target_2 = 6  # [1,3]
    numbers_3 = [-1, 0]
    target_3 = -1  # [1,2]
    print(Solution().twoSum(numbers_1, target_1))
    print(Solution().twoSum(numbers_2, target_2))
    print(Solution().twoSum(numbers_3, target_3))
    """
    doctest.testmod(verbose=True)
