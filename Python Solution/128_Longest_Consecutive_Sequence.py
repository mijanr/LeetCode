"""
Author: Md Mijanur Rahman
Date: 04/12/2022
Difficulty: Medium
Problem Link: https://leetcode.com/problems/longest-consecutive-sequence/
Problem Description: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        >>> Solution().longestConsecutive([100,4,200,1,3,2])
        4
        >>> Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1])
        9
        >>> Solution().longestConsecutive([1,2,0,1])
        3
        >>> Solution().longestConsecutive([])
        0
        """
        hashSet = set(nums)
        if not nums:
            return 0
        current_max = 1
        for num in nums:
            if num-1 not in hashSet:
                current_num = num
                count = 1
                while current_num+1 in hashSet:
                    current_num += 1
                    count += 1
                current_max = max(count, current_max)
        return current_max

if __name__ == "__main__":
    import doctest
    doctest.testmod()