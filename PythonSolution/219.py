from typing import List
import doctest

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        >>> s = Solution()
        >>> s.containsNearbyDuplicate([1,2,3,1], 3)
        True
        >>> s.containsNearbyDuplicate([1,0,1,1], 1)
        True
        >>> s.containsNearbyDuplicate([1,2,3,1,2,3], 2)
        False
        """
        hashmap = {}
        for idx, num in enumerate(nums):
            if num in hashmap and abs(idx-hashmap[num])<=k:
                return True
            else:
                hashmap[num] = idx
        return False
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)