from typing import List
import doctest

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        >>> s = Solution()
        >>> s.longestCommonPrefix(["flower","flow","flight"])
        'fl'
        >>> s.longestCommonPrefix(["dog","racecar","car"])
        ''
        >>> s.longestCommonPrefix([""])
        ''
        >>> s.longestCommonPrefix(["a"])
        'a'
        """
        #find the shortest string
        prefix = min(strs, key=len)
        #iterate through the shortest string
        for i in range(len(prefix)):
            #check if all the other strings have the same character at the same index
            if all(x[i] == prefix[i] for x in strs):
                continue
            else:
                return prefix[:i]
        return prefix
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)