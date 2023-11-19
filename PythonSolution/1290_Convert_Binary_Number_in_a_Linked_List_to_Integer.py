"""
Author: Md Mijanur Rahman
Date: 19/11/2023
Difficulty: Easy
Problem Link: 
    https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
Problem Description:
    Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
    Return the decimal value of the number in the linked list.
    The most significant bit is at the head of the linked list.
"""
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current = head
        binary = ''
        while current:
            binary += str(current.val)
            current = current.next
        return int(binary, 2)
    
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(0)
    head.next.next = ListNode(1)
    print(Solution().getDecimalValue(head))



        