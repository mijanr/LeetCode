from typing import List
import doctest

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        >>> sol = Solution()
        >>> sol.nextGreaterElement([4,1,2], [1,3,4,2])
        [-1, 3, -1]
        >>> sol.nextGreaterElement([2,4], [1,2,3,4])
        [3, -1]
        """
        hashMap = {}
        for idx, num in enumerate(nums2):
            hashMap[num] = nums2[idx+1:]
        sol = []
        for idx, num in enumerate(nums1):
            lst = hashMap[num]
            for n in lst:
                if n>num:
                    sol.append(n)
                    break
            else:
                sol.append(-1)
        return sol
    
if __name__ == '__main__':
    doctest.testmod(verbose=True)     