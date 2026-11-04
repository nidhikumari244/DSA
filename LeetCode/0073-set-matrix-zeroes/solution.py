class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m= len(matrix)
        n= len(matrix[0])

        row = [False] * m
        col = [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row [i] = True 
                    col[j] = True 

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] =0
