class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """

        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0

        for j in range(1, n + 1):
            for d in (1, 2, 3):
                i = j - d
                if i >= 0:
                    dp[j] = min(dp[j], dp[i] + costs[j - 1] + d * d)

        return dp[n]
