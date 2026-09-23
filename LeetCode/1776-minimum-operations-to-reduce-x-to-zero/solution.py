class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        n = len(nums)
        left = 0
        window_sum = 0
        best = -1

        for right in range(n):
            window_sum += nums[right]

            while window_sum > target and left <= right:
                window_sum -= nums[left]
                left += 1

            if window_sum == target:
                best = max(best, right - left + 1)

        return n - best if best != -1 else -1
