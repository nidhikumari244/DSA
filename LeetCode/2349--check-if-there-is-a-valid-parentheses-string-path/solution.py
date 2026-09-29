class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])

        # total path length m+n-1 must be even for any balanced string
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        # dp[i][j] = set of possible balances (opens - closes) reachable at (i, j)
        dp = [[None] * n for _ in range(m)]
        dp[0][0] = set([1])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                delta = 1 if grid[i][j] == '(' else -1
                cur = set()
                if i > 0 and dp[i - 1][j]:
                    for b in dp[i - 1][j]:
                        nb = b + delta
                        if nb >= 0:
                            cur.add(nb)
                if j > 0 and dp[i][j - 1]:
                    for b in dp[i][j - 1]:
                        nb = b + delta
                        if nb >= 0:
                            cur.add(nb)
                dp[i][j] = cur if cur else None

        last = dp[m - 1][n - 1]
        return last is not None and 0 in last
