class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m, n = len(grid), len(grid[0])
        dp = [None] * n
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                if i == 0 and j == 0:
                    dp[j] = {v}
                    continue
                cur = set()
                if i > 0:
                    for x in dp[j]:
                        cur.add(x ^ v)
                if j > 0:
                    for x in dp[j - 1]:
                        cur.add(x ^ v)
                dp[j] = cur
        return min(dp[n - 1])
