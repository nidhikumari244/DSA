class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        k=k%len(nums)


        left = 0
        right = len(nums)-1
        while left < right :
            nums[left],nums[right]=nums[right],nums[left]
            left +=1
            right-=1

        left = 0
        right = k-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1

        left = k
        right= len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1  
