'''
Author: Md Mijanur Rahman
Date: 22/06/2023
Difficulty: Easy
Problem Link: https://leetcode.com/problems/remove-element/
Problem Description: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
                    The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
'''

import doctest
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        >>> Solution().removeElement([3,2,2,3], 3)
        2
        >>> Solution().removeElement([0,1,2,2,3,0,4,2], 2)
        5
        """
        res = 0
        for num in nums:
            if num!=val:
                res += 1
        return res

if __name__ == "__main__":
    doctest.testmod(verbose=True)
    # print(Solution().removeElement([3,2,2,3], 3))
    # print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))