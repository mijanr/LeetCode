import doctest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        >>> s = Solution()
        >>> s.lengthOfLongestSubstring("abcabcbb")
        3
        >>> s.lengthOfLongestSubstring("bbbbb")
        1
        >>> s.lengthOfLongestSubstring("pwwkew")
        3
        """
        hashmap = {}
        max_len = 0
        start = 0
        end = 0
        while end < len(s):
            if s[end] not in hashmap:
                hashmap[s[end]] = end
                #print(hashmap)
                end += 1
                max_len = max(max_len, end - start)
            else:
                #remove the start index
                del hashmap[s[start]]
                start += 1
        return max_len 
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)