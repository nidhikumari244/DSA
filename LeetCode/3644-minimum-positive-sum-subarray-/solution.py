class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        best = float('inf')
        for i in range(n):
            for length in range(l, r + 1):
                j = i + length
                if j > n:
                    break
                s = prefix[j] - prefix[i]
                if s > 0 and s < best:
                    best = s

        return -1 if best == float('inf') else best
