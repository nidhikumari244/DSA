class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)



        for i in range(n):
            left_max = max(nums[:i + 1])
            right_min = min(nums[i:])

            instability = left_max - right_min

            if instability <= k:
                return i

        return -1
