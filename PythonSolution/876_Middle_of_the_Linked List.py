"""
Author: Md Mijanur Rahman
Date: 19/11/2023
Difficulty: Easy
Problem Link: https://leetcode.com/problems/middle-of-the-linked-list/description/
Problem Description: Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        leng = 0
        curr_node = head
        while curr_node:
            leng += 1
            curr_node = curr_node.next        
        leng = leng//2+1
        
        i=1
        curr = head
        while curr and i<leng:
            middle = curr.val
            curr = curr.next
            i += 1
        return curr
    
if __name__ == "__main__":
    pass

        
    
        