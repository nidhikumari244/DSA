class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1  
        found = False
        for i, x in enumerate(nums):
            if x != i:
                res &= x
                found = True
        return res if found else 0
