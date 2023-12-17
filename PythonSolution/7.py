import doctest

class Solution:
    def reverse(self, x: int) -> int:
        """
        >>> s = Solution()
        >>> s.reverse(123)
        321
        >>> s.reverse(-123)
        -321
        >>> s.reverse(120)
        21
        >>> s.reverse(0)
        0
        """
        if abs(x)<10:
            return x
        else:
            y = x
            x = abs(x)
            lst=[]
            keep = True
            while keep:
                if x%10!=0 or len(lst)!=0:
                    lst.append(x%10)
                x = x//10
                if x<10:
                    lst.append(x)
                    keep = False

            ans = 0
            for idx, num in enumerate(reversed(lst)):
                ans += num*10**idx
            if y<0:
                ans = -ans
            if ans >= 2 ** 31 - 1 or ans <= -2 ** 31:  
                return 0
            else:   
                return ans
            
if __name__ == "__main__":
    doctest.testmod(verbose=True)