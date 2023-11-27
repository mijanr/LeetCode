import doctest

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """
        >>> s = Solution()
        >>> s.kthFactor(12,3)
        3
        >>> s.kthFactor(7,2)
        7
        >>> s.kthFactor(4,4)
        -1
        """
        factors = [factor for factor in range(1,n+1) if n%factor==0]
        if len(factors)<k:
            return -1
        return factors[k-1]

if __name__ == "__main__":
    doctest.testmod(verbose=True)
        