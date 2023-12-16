import numpy as np
from typing import List
import doctest

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        >>> s = Solution()
        >>> s.findMedianSortedArrays([1, 3], [2])
        2.00000
        >>> s.findMedianSortedArrays([1, 2], [3, 4])
        2.50000
        """
        num1 = np.array(nums1)
        num2 = np.array(nums2)
        nums = np.concatenate((num1, num2))
        nums.sort()
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
        return nums[len(nums) // 2]
    
if __name__ == "__main__":
    pass