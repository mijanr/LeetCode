from typing import List
import doctest

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """
        >>> s = Solution()
        >>> s.sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170])
        ['Mary', 'Emma', 'John']
        >>> s.sortPeople(names = ["Alice","Bob","Bob"], heights = [155,185,150])
        ['Bob', 'Alice', 'Bob']
        """
        hashMap = {}
        for name, height in zip(names, heights):
            hashMap[height] = name
        heights.sort()
        return [hashMap[height] for height in heights[::-1]]
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)