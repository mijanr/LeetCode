"""
Author: Md Mijanur Rahman
Date: 20/11/2023
Difficulty: Easy
Problem Link: https://leetcode.com/problems/palindrome-linked-list/description/
Problem Description: Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        nums = []
        while curr:
            nums.append(curr.val)
            curr = curr.next
        return nums == nums[::-1]
    
if __name__ == "__main__":
    pass
