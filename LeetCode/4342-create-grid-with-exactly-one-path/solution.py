class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid = ['.' * n]
        for _ in range(m - 1):
            grid.append('#' * (n - 1) + '.')
        return grid
        
