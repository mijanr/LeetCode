"""
Author: Md Mijanur Rahman
Date: 21/11/2023
Difficulty: Easy
Problem Link: https://leetcode.com/problems/reverse-words-in-a-string/description/
Problem Description: Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be 
separated by at least one space. Return a string of the words in reverse order 
concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. 
Do not include any extra spaces.
"""
import doctest

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        >>> Solution().reverseWords("the sky is blue")
        'blue is sky the'
        >>> Solution().reverseWords("  hello world  ")
        'world hello'
        >>> Solution().reverseWords("a good   example")
        'example good a'
        >>> Solution().reverseWords("  Bob    Loves  Alice   ")
        'Alice Loves Bob'
        """
        return " ".join(s.split()[::-1])
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)
    


        