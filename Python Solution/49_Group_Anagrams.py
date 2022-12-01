"""
Author: Md Mijanur Rahman
Date: 01/12/2022
Difficulty: Medium
Problem Link: https://leetcode.com/problems/group-anagrams/
Problem Description: Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        >>> Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        >>> Solution().groupAnagrams([""])
        [['']]
        >>> Solution().groupAnagrams(["a"])
        [['a']]
        """
        hashMap = {}
        for st in strs:
            tp = tuple(sorted(st))
            if tp not in hashMap:
                hashMap[tp] = [st]
            else:
                hashMap[tp].append(st)
        return list(hashMap.values())

if __name__ == "__main__":
    import doctest
    doctest.testmod()
        

