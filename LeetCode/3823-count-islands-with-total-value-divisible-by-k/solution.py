class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c):
            if (r < 0 or r >= m or c < 0 or c >= n
                    or grid[r][c] == 0 or visited[r][c]):
                return 0

            visited[r][c] = True
            total = grid[r][c]

            total += dfs(r - 1, c)  # Up
            total += dfs(r + 1, c)  # Down
            total += dfs(r, c - 1)  # Left
            total += dfs(r, c + 1)  # Right

            return total

        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not visited[r][c]:
                    island_sum = dfs(r, c)

                    if island_sum % k == 0:
                        count += 1

        return count

