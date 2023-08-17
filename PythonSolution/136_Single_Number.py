"""
Author: Md Mijanur Rahman
Date: 29/11/2022
Difficulty: Easy
Problem Link: https://leetcode.com/problems/single-number/description/
Problem Description: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hashMap = {}
        # for num in nums:
        #     if num not in hashMap:
        #         hashMap[num] = 1
        #     else:
        #         hashMap[num] += 1
        # for key, val in hashMap.items():
        #     if val==1:
        #         return key
        """
        Let's try another approach: bitwise XOR
        If we take XOR of zero and some bit, it will return that bit. i.e. a⊕0=a
        If we take XOR of two same bits, it will return 0. i.e. a⊕a=0
        a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
        Now let's say we have a list [2,2,1]. If we store our result res=0 and then XOR it with each element in the list, we will get the following:
        res=0⊕2=2
        res=2⊕2=0
        res=0⊕1=1
        Elegenat, right? We can use this approach to solve the problem.
        """
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__ == "__main__":
    nums_1 = [2, 2, 1]  # 1
    nums_2 = [4, 1, 2, 1, 2]  # 4
    nums_3 = [1]  # 1
    solution = Solution()
    for nums in [nums_1, nums_2, nums_3]:
        print(solution.singleNumber(nums))
