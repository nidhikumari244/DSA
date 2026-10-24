class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        previous=[1]
        for newrow in range(rowIndex):
            current=[1]
            for i in range(len(previous)-1):
                current.append(previous[i]+previous[1+i])
            current.append(1)
            previous=current
        return previous 
            

