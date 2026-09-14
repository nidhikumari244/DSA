class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        

        nums.sort()
        left = 0
        window_sum = 0
        best = 1
        
        for right in range(len(nums)):
            window_sum += nums[right]
            
            # Cost to raise everyone in [left, right] up to nums[right]:
            # nums[right] * (window_size) - window_sum
            while nums[right] * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1
            
            best = max(best, right - left + 1)
        
        return best
