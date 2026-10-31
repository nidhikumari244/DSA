class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        R = [[0] * (n + 1) for _ in range(m + 1)]
        D = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    tot = 1
                    R[i][j + 1] = (R[i][j + 1] + tot) % MOD
                    D[i + 1][j] = (D[i + 1][j] + tot) % MOD
                    continue
                if grid[i][j] == 0:
                    tot = (R[i][j] + D[i][j]) % MOD
                    if i == m - 1 and j == n - 1:
                        return tot
                    R[i][j + 1] = (R[i][j + 1] + tot) % MOD
                    D[i + 1][j] = (D[i + 1][j] + tot) % MOD
                else:
                    D[i + 1][j] = (D[i + 1][j] + R[i][j]) % MOD
                    R[i][j + 1] = (R[i][j + 1] + D[i][j]) % MOD
        return 0
