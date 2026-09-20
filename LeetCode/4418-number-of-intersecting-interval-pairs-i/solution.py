class Solution(object):
    def countIntersectingIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        count=0
        n=len(intervals)
        for i in range(n):
            for j in range(i+1,n):
                if intervals[i][1]>= intervals[j][0] and intervals[j][1] >= intervals[i][0]:
                    count+=1
        return count  
