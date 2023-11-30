import doctest
class Solution:
    def isUgly(self, n: int) -> bool:
        """
        >>> s = Solution()
        >>> s.isUgly(6)
        True
        >>> s.isUgly(8)
        True
        >>> s.isUgly(14)
        False
        >>> s.isUgly(1)
        True
        >>> s.isUgly(0)
        False
        >>> s.isUgly(-1)
        False
        """
        if n==1:
            return True
        if n<= 0:
            return False
        
        while True:
            if n%2==0:
                n /= 2
            elif n%3==0:
                n /= 3
            elif n%5==0:
                n /= 5
            elif n==1:
                return True
            else:
                return False
            
if __name__ == "__main__":
    doctest.testmod(verbose=True)
        
        