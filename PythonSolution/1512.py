from typing import List
import doctest

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.numIdenticalPairs([1,2,3,1,1,3])
        4
        >>> s.numIdenticalPairs([1,1,1,1])
        6
        >>> s.numIdenticalPairs([1,2,3])
        0
        """
        count = 0
        for idx, num in enumerate(nums):
            for i in range(idx+1, len(nums)):
                if num == nums[i]:
                    count += 1
        return count
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)