"""
Author: Md Mijanur Rahman
Date: 18/11/2023
Difficulty: Easy
Problem Link: https://leetcode.com/problems/power-of-two/description/
Problem Description: Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2^x.
"""

import doctest

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        >>> Solution().isPowerOfTwo(1)
        True
        >>> Solution().isPowerOfTwo(16)
        True
        >>> Solution().isPowerOfTwo(3)
        False
        >>> Solution().isPowerOfTwo(4)
        True
        >>> Solution().isPowerOfTwo(5)
        False
        >>> Solution().isPowerOfTwo(0)
        False
        """
        if n<=0:
            return False
        if n==1:
            return True
        while n%2==0:
            if n==2:
                return True
            n = n//2
        return False

            
if __name__ == "__main__":
    doctest.testmod(verbose=True)