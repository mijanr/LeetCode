from typing import List
import doctest

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """
        >>> s = Solution()
        >>> s.applyOperations([1,2,2,1,1,0])
        [1, 4, 2, 0, 0, 0]
        >>> s.applyOperations([0,0,0,0,0,0])
        [0, 0, 0, 0, 0, 0]
        >>> s.applyOperations([1,1,1,1,1,1])
        [2, 2, 2, 0, 0, 0]
        >>> s.applyOperations([1,2,3,4,5,6])
        [1, 2, 3, 4, 5, 6]
        >>> s.applyOperations([0,1])
        [1, 0]
        """
        for idx in range(len(nums)-1):
            if nums[idx]==nums[idx+1]:
                nums[idx] *= 2
                nums[idx+1] = 0 
        length = len(nums)
        nums = [num for num in nums if num!=0]
        for num in range(length-len(nums)):
            nums.append(0)
        return nums      
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)