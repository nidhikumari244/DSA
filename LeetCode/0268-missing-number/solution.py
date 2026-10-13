class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        original_no = n*(n+1)//2
        missing_no = original_no - sum(nums)
        return missing_no
