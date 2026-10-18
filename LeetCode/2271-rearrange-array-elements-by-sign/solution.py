class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos= 0
        neg = 1
        result= [0]* len(nums)
        for i in range ( 0, len(nums)):
            if nums[i]> 0:
                result[pos]=nums[i]
                pos+=2
            else:
                result[neg] = nums[i]
                neg+=2
        return result


