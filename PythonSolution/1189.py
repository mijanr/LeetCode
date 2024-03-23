"""
Author: Md Mijanur Rahman
Date: 23/03/2024
Difficulty: Easy
Problem Link: https://leetcode.com/problems/maximum-number-of-balloons/
Problem Description: Given a string text, you want to use the characters of text to form as many instances of 
the word "balloon" as possible. You can use each character in text at most once. Return the maximum number of 
instances that can be formed.
"""
import pytest

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        >>> s = Solution()
        >>> s.maxNumberOfBalloons("nlaebolko")
        1
        >>> s.maxNumberOfBalloons("loonbalxballpoon")
        2
        >>> s.maxNumberOfBalloons("leetcode")
        0
        """

        hashMap = {}
        for t in text:
            if t not in hashMap:
                hashMap[t] = 1
            else:
                hashMap[t] += 1
        print(hashMap)
        b = hashMap.get('b', 0)
        a = hashMap.get('a', 0)
        l = hashMap.get('l', 0)
        o = hashMap.get('o', 0)
        n = hashMap.get('n', 0)
        return min(b, a, l//2, o//2, n)
    
def test_maxNumberOfBalloons():
    s = Solution()
    assert s.maxNumberOfBalloons("nlaebolko") == 1
    assert s.maxNumberOfBalloons("loonbalxballpoon") == 2
    assert s.maxNumberOfBalloons("leetcode") == 0
    
if __name__ == "__main__":
    pass