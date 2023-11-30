import doctest

class Solution:
    def countPrimes(self, n):
        """
        >>> sol = Solution()
        >>> sol.countPrimes(10)
        4
        >>> sol.countPrimes(0)
        0
        >>> sol.countPrimes(1)
        0
        >>> sol.countPrimes(2)
        0
        >>> sol.countPrimes(100)
        25
        """
        if n<2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
        return sum(primes)
    
if __name__ == '__main__':
    doctest.testmod(verbose=True)