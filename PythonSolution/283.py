from typing import List
import doctest

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_elements = [num for num in nums if num!=0]
        for idx in range(len(nums)):
            if idx < len(non_zero_elements):
                nums[idx] = non_zero_elements[idx]
            else:
                nums[idx] = 0

if __name__ == "__main__":
    pass