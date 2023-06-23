"""
Author: Md Mijanur Rahman
Date: 28/11/2022
Difficulty: Medium
Problem Link: https://leetcode.com/problems/top-k-frequent-elements/
Problem Description: Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol_dict = {}
        for num in nums:
            if num not in sol_dict:
                sol_dict[num] = 1
            else:
                sol_dict[num] += 1
        sorted_dict = dict(
            sorted(sol_dict.items(), key=lambda x: x[1], reverse=True)[:k]
        )
        return list(sorted_dict.keys())


if __name__ == "__main__":
    nums_1 = [1, 1, 1, 2, 2, 3]
    k_1 = 2  # Output: [1,2]
    nums_2 = [1]
    k_2 = 1  # Output: [1]
    print(Solution().topKFrequent(nums_1, k_1))
    print(Solution().topKFrequent(nums_2, k_2))
