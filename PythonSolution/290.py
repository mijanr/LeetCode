
import doctest

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        >>> s = Solution()  
        >>> s.wordPattern("abba", "dog cat cat dog")
        True
        >>> s.wordPattern("abba", "dog cat cat fish")
        False
        >>> s.wordPattern("aaaa", "dog cat cat dog")
        False
        >>> s.wordPattern("abba", "dog dog dog dog")
        False
        """
        if len(pattern)!=len(s.split(" ")):
            return False
        hashmap = {}
        for ch, c in zip(pattern, s.split(" ")):
            if ch not in hashmap:
                hashmap[ch] = c
            else:
                if hashmap[ch] != c:
                    return False
        if len(set(hashmap.values())) != len(set(pattern)):
            return False
        return True
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)
        

