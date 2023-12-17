import doctest  
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.maxArea([1,8,6,2,5,4,8,3,7])
        49
        >>> s.maxArea([1,1])
        1
        """
        area = 0
        update = True
        i = 0
        j = len(height) - 1
        while update:
            if height[i] < height[j]:
                area = max(area, height[i] * (j - i))
                i += 1
            else:
                area = max(area, height[j] * (j - i))
                j -= 1
            if i == j:
                update = False
        return area
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)