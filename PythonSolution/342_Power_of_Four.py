"""
Author: Md Mijanur Rahman
Date: 18/11/2023
Difficulty: Easy
Problem Link: https://leetcode.com/problems/power-of-four/description/
Problem Description: Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4^x.
"""

import doctest

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        >>> Solution().isPowerOfFour(16)
        True
        >>> Solution().isPowerOfFour(5)
        False
        >>> Solution().isPowerOfFour(1)
        True
        >>> Solution().isPowerOfFour(0)
        False
        """
        if n<=0:
            return False
        if n==1:
            return True
        while n%4==0:
            if n==4:
                return True
            n = n//4
        return False
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)
        