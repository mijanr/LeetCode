import doctest

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        >>> s = Solution()
        >>> s.isPerfectSquare(16)
        True
        >>> s.isPerfectSquare(14)
        False
        >>> s.isPerfectSquare(1)
        True
        >>> s.isPerfectSquare(100)
        True
        >>> s.isPerfectSquare(99)
        False
        """
        n = 1
        while True:
            if n**2==num:
                return True
            if n**2 > num:
                break
            else:
                n += 1
        return False
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)            