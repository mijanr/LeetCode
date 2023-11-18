"""
Author: Md Mijanur Rahman
Date: 18/11/2023
Difficulty: Easy
Problem Link: https://leetcode.com/problems/power-of-three/description/
Problem Description: Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x.
"""
import doctest

class Solution:
    def isPowerOfThree(self, num: int) -> bool:
        """
        >>> Solution().isPowerOfThree(27)
        True
        >>> Solution().isPowerOfThree(0)
        False
        >>> Solution().isPowerOfThree(9)
        True
        >>> Solution().isPowerOfThree(45)
        False
        >>> Solution().isPowerOfThree(-3)
        False
        >>> Solution().isPowerOfThree(1)
        True
        """
        if num <=0:
            return False
        if num==1 or num==3:
            return True
        while num%3==0:
            num = num//3
            if num==3:
                return True
        if num==0:
            return True
        else:
            return False
        
if __name__ == "__main__":
    doctest.testmod(verbose=True)
    
        
