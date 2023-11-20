"""
Author: Md Mijanur Rahman
Date: 20/11/2023
Difficulty: Easy
Problem Link: https://leetcode.com/problems/reverse-linked-list/description/
Problem Description: Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        while stack:
            curr.val = stack.pop()
            curr = curr.next
        return head
    
if __name__ == "__main__":
    pass
    
        