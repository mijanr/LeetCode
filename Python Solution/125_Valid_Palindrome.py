"""
Author: Md Mijanur Rahman
Date: 30/11/2022
Difficulty: Easy
Problem Link: https://leetcode.com/problems/valid-palindrome/
Problem Description: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(e for e in s if e.isalnum())
        s = s.lower()
        i_max = len(s) // 2
        if len(s) <= 1:
            return True
        i, j = 0, -1
        while True:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            if i == i_max:
                return True


if __name__ == "__main__":
    s_1 = "A man, a plan, a canal: Panama"  # True
    s_2 = "race a car"  # False
    s_3 = " "  # True
    solution = Solution()
    print(solution.isPalindrome(s_1))
    print(solution.isPalindrome(s_2))
    print(solution.isPalindrome(s_3))
