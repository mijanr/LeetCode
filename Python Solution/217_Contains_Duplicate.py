'''
Author: Md Mijanur Rahman
Date: 28/11/2022
Difficulty: Easy
Problem Link: https://leetcode.com/problems/contains-duplicate/
Problem Description: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result_dict = {}
        for num in nums:
            if num in result_dict:
                return True
            else:
                result_dict[num] = 0
        return False

if __name__ == "__main__":
    nums_1 = [1,2,3,1] # True
    nums_2 = [1,2,3,4] # False
    nums_3 = [1,1,1,3,3,4,3,2,4,2] # True

    solution = Solution()
    for nums in [nums_1, nums_2, nums_3]:
        print(solution.containsDuplicate(nums))
