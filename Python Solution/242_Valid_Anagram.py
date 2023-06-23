"""
Author: Md Mijanur Rahman
Date: 28/11/2022
Difficulty: Easy
Problem Link: https://leetcode.com/problems/valid-anagram/
Problem Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        t_dict = {}
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        for key, val in s_dict.items():
            if len(t_dict.keys()) != len(s_dict.keys()):
                return False
            if key in t_dict and t_dict[key] < val or key not in t_dict:
                return False
        return True


if __name__ == "__main__":
    s_1 = "anagram"
    t_1 = "nagaram"  # True
    s_2 = "rat"
    t_2 = "car"  # False
    s_3 = "a"
    t_3 = "ab"  # False
    solution = Solution()
    print(solution.isAnagram(s_1, t_1))
    print(solution.isAnagram(s_2, t_2))
    print(solution.isAnagram(s_3, t_3))
