class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = nums[0]
        best = -1

        if all(nums[i] == (s + i) % n for i in range(n)):
            if s == 0:
                return 0
            best = min(n - s, s + 2)

        if all(nums[i] == (s - i) % n for i in range(n)):
            cost = 1 + min((n - s - 1) % n, (s + 1) % n)
            best = cost if best == -1 else min(best, cost)

        return best
