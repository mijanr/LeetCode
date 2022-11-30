'''
Author: Md Mijanur Rahman
Date: 29/11/2022
Difficulty: Easy
Problem Link: https://leetcode.com/problems/single-number/description/
Problem Description: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        for key, val in hashMap.items():
            if val==1:
                return key

if __name__=='__main__':
    nums_1 = [2,2,1] # 1
    nums_2 = [4,1,2,1,2] # 4
    nums_3 = [1] # 1
    solution = Solution()
    for nums in [nums_1, nums_2, nums_3]:
        print(solution.singleNumber(nums))