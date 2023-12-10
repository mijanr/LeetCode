from typing import List
import doctest

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        >>> s = Solution()
        >>> s.smallerNumbersThanCurrent([8,1,2,2,3])
        [4, 0, 1, 1, 3]
        >>> s.smallerNumbersThanCurrent([6,5,4,8])
        [2, 1, 0, 3]
        >>> s.smallerNumbersThanCurrent([7,7,7,7])
        [0, 0, 0, 0]
        """
        res = []
        for num in nums:
            count = 0
            for num1 in nums:
                if num != num1 and num1<num:
                    count += 1
            res.append(count)
        return res
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)

        