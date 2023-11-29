import math 
import doctest

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        >>> s = Solution()
        >>> s.judgeSquareSum(5)
        True
        >>> s.judgeSquareSum(3)
        False
        >>> s.judgeSquareSum(4)
        True
        >>> s.judgeSquareSum(0)
        True
        >>> s.judgeSquareSum(1)
        True
        >>> s.judgeSquareSum(2)
        True
        """
        b = 0
        a = 0
        while a>=0:
            a = c - b**2
            if a < 0:
                return False
            if math.sqrt(a).is_integer():
                return True
            b += 1
        return False
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)