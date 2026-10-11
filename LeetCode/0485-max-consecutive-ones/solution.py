class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count =0
        maximum=0

        for i in range(0,len(nums)):
            if nums[i]==1:
                count+=1
                maximum = max(maximum,count)
            if nums[i]==0:
                count=0
        return maximum 
        
