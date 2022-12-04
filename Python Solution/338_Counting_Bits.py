"""
Author: Md Mijanur Rahman
Date: 04/12/2022
Difficulty: Easy
Problem Link: https://leetcode.com/problems/counting-bits/
Problem Description: Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""

from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        >>> Solution().countBits(2)
        [0, 1, 1]
        >>> Solution().countBits(5)
        [0, 1, 1, 2, 1, 2]
        """
        return [bin(i)[2:].count('1') for i in range(n+1)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()