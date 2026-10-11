class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total =0
        
        for i in range (0,len(nums)):
            if len(nums) % (i+1) == 0:
                total += nums[i] * nums[i] 
        return total 

