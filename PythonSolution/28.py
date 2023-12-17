import doctest
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        >>> s = Solution()
        >>> s.strStr("sadbutsad", "sad")
        0
        >>> s.strStr("leetcode", "leeto")
        -1
        """
        if len(needle)==0:
            return 0
        for idx, _ in enumerate(haystack):
            if needle == haystack[idx:idx+len(needle)]:
                return idx
        return -1
        
if __name__ == "__main__":
    doctest.testmod(verbose=True)