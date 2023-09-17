"""
Author: Md Mijanur Rahman
Date: 22/06/2023
Difficulty: Easy
Problem Link: https://leetcode.com/problems/palindrome-number/
Problem Description: Given an integer x, return true if x is palindrome integer.
"""
import doctest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        >>> Solution().isPalindrome(121)
        True
        >>> Solution().isPalindrome(-121)
        False
        >>> Solution().isPalindrome(10)
        False
        >>> Solution().isPalindrome(-101)
        False
        """
        if x<0:
          return False
        if str(x)==str(x)[::-1]:
          return True
        else:
          return False


if __name__ == "__main__":
    doctest.testmod(verbose=True)
