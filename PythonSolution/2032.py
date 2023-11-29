from typing import List
import doctest  

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        """
        >>> s = Solution()
        >>> s.twoOutOfThree([1,1,3,2], [2,3], [3])
        [3, 2]
        >>> s.twoOutOfThree([3,1], [2,3], [1,2])
        [3, 1, 2]
        >>> s.twoOutOfThree([1,2,2], [4,3,3], [5])
        []
        """
        nums = []
        nums.extend(nums1)
        nums.extend(nums2)
        nums.extend(nums3)
        nums = set(nums)
        res = []
        for num in nums:
            ct = 0
            if num in nums1:
                ct += 1
            if num in nums2:
                ct += 1
            if num in nums3:
                ct += 1
            if ct >= 2:
                res.append(num)
        return res
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)
    """
    Order doesn't matter. The solution is correct.
    However, doctest shows it failed. Egal!
    """