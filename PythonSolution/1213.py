from typing import List
import doctest

class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        """
        >>> s = Solution()
        >>> s.arraysIntersection([1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8])
        [1, 5]
        >>> s.arraysIntersection([1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8,9])
        [1, 5]
        """
        return [num for num in arr1 if num in arr2 and num in arr3]
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)
    
