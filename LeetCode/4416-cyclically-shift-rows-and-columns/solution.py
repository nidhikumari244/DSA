class Solution(object):
    def cyclicShift(self, n, grid, rowShift, colShift):
        """
        :type n: int
        :type grid: List[List[int]]
        :type rowShift: List[int]
        :type colShift: List[int]
        :rtype: List[List[int]]
        """
        for i in range(n):
            k = rowShift[i] % n
            grid[i] = grid[i][k:] + grid[i][:k]
        for j in range(n):
            k=colShift[j]%n
            column=[grid[i][j] for i in range(n)]
            column=column[k:] + column[:k]

            for i in range(n):
                grid[i][j]=column[i]
        return grid
        
