"""
Author: Md Mijanur Rahman
Date: 29/06/2023
Difficulty: Easy
Problem Link: https://leetcode.com/problems/length-of-last-word/
Problem Description: Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
"""
import doctest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        >>> Solution().lengthOfLastWord("Hello World")
        5
        >>> Solution().lengthOfLastWord("   fly me   to   the moon  ")
        4
        >>> Solution().lengthOfLastWord("luffy is still joyboy")
        6

        """
        return len(s.split()[-1])


if __name__ == "__main__":
    # print(Solution().lengthOfLastWord("Hello World"))
    doctest.testmod(verbose=True)
