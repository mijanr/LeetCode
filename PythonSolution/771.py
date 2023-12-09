import doctest

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        >>> s = Solution()
        >>> s.numJewelsInStones("aA", "aAAbbbb")
        3
        >>> s.numJewelsInStones("z", "ZZ")
        0
        """
        ans = 0
        for s in stones:
            for j in jewels:
                if s==j:
                    ans += 1
        return ans

if __name__ == "__main__":
    doctest.testmod(verbose=True)
        