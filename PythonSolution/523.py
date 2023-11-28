from typing import List
import doctest

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        >>> s = Solution()
        >>> s.checkSubarraySum([23,2,4,6,7], 6)
        True
        >>> s.checkSubarraySum([23,2,6,4,7], 6)
        True
        >>> s.checkSubarraySum([23,2,6,4,7], 13)
        False
        """
        for idx1, num1 in enumerate(nums):
            currSum = num1
            for idx2, num2 in enumerate(nums[idx1+1:]):
                currSum += num2
                if currSum%k==0:
                    return True
        return False
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)