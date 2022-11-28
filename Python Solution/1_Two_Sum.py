'''
Author: Md Mijanur Rahman
Date: 28/11/2022
Difficulty: Easy
Problem Link: https://leetcode.com/problems/two-sum/
Problem Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
'''

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol_dict = {}
        for idx, num in enumerate(nums):
            if num not in sol_dict:
                sol_dict[target-num] = idx
            else:
                return [idx, sol_dict[num]]
if __name__=='__main__':
    nums_1 = [2,7,11,15]
    target_1 = 9 # [0,1]
    nums_2 = [3,2,4]
    target_2 = 6 # [1,2]
    nums_3 = [3,3]
    target_3 = 6 # [0,1]

    solution = Solution()
    for nums, target in [(nums_1, target_1), (nums_2, target_2), (nums_3, target_3)]:
        print(solution.twoSum(nums, target))

        