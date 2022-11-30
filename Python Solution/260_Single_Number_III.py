"""
Author: Md Mijanur Rahman
Date: 30/11/2022
Difficulty: Medium
Problem Link: https://leetcode.com/problems/single-number-iii/description/
Problem Description: Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
"""
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        return [key for key, val in hashMap.items() if val==1]

if __name__ == "__main__":
    nums_1 = [1,2,1,3,2,5] # Output: [3,5]
    nums_2 = [-1,0] # Output: [-1,0]
    nums_3 = [0,1] # Output: [1,0]
    solution = Solution()
    for nums in [nums_1, nums_2, nums_3]:
        print(solution.singleNumber(nums))
