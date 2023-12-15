import doctest

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        >>> s = Solution()
        >>> s.romanToInt('III')
        3
        >>> s.romanToInt('IV')
        4
        >>> s.romanToInt('IX')
        9
        """
        hashmap_u = {'I':1,'V':5,'X':10,'L':50, 'C':100,'D':500, 'M':1000}
        hashmap_c = {'IV':4,'IX':9,'XL':40,'XC':90, 'CD':400,'CM':900}
        sum = 0
        keep = True
        i = 0
        while keep:
            if s[i:i+2] in hashmap_c:
                sum += hashmap_c[s[i:i+2]]
                i += 2
            else:
                sum += hashmap_u[s[i]]
                i += 1
            if i == len(s):
                keep = False
        return sum
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)
    
