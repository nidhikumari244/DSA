class Solution(object):
    def countIntersectingIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        import bisect
        intervals.sort()
        
      

        temoravlin = intervals

        ends = []
        count = 0

        for start, end in intervals:
            pos = bisect.bisect_left(ends, start)

           
            count += len(ends) - pos

            bisect.insort(ends, end)

        return count
