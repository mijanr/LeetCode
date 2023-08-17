"""
Author: Md Mijanur Rahman
Date: 30-11-2022
Difficulty: Easy
Problem Link: https://leetcode.com/problems/happy-number/
Problem Description: Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()
        while n != 1:
            if n in hashSet:
                return False
            hashSet.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return True


if __name__ == "__main__":
    n_1 = 19  # True
    n_2 = 2  # False

    print(Solution().isHappy(n_1))
    print(Solution().isHappy(n_2))
