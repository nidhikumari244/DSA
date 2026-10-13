class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        suq= sorted (x*x for x in nums)
        n= len(suq)
        k=(n+1)//2
        return sum(suq[n-k:]) - sum(suq[:n-k])
