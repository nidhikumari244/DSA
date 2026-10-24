class Solution(object):
    def generate(self,numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle=[[1]]

        for newrow in range(numRows-1):
            previous=triangle[-1]
            current=[1]
            for i in range (len(previous)-1):
                current.append(previous[i]+previous[1+i])
            current.append(1)
            triangle.append(current)
        return triangle

