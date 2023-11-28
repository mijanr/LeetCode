from typing import List
import doctest

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        >>> s = Solution()
        >>> s.subarraySum([1,1,1], 2)
        2
        >>> s.subarraySum([1,2,3], 3)
        2
        >>> s.subarraySum([1,2,3], 4)
        0
        >>> s.subarraySum([1,2,3], 5)
        1
        >>> s.subarraySum([1,2,3], 6)
        1
        >>> s.subarraySum([1,2,3], 7)
        0
        >>> s.subarraySum([1,-1,0], 0)
        3
        >>> s.subarraySum([1,-1,0], 1)
        1
        """
        sol = 0
        for idx1, num1 in enumerate(nums):
            curr_sum = num1
            if curr_sum == k:
                sol+=1
            for idx2, num2 in enumerate(nums[idx1+1:]):
                curr_sum += num2
                if curr_sum == k:
                    sol+=1
        return sol
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)

        