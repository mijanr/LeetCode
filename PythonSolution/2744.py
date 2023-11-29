from typing import List 
import doctest

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        """
        >>> s = Solution()
        >>> s.maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"])
        2
        >>> s.maximumNumberOfStringPairs(["ab","ba","cc"])
        1
        >>> s.maximumNumberOfStringPairs(["aa","ab"])
        0
        """
        cnt = 0
        for idx1, word1 in enumerate(words):
            for idx2, word2 in enumerate(words[idx1+1:]):
                if word1 == word2[::-1]:
                    cnt += 1
        return cnt
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)