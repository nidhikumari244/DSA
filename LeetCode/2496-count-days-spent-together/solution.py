class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """

        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def dayOfYear(date):
            month = int(date[:2])
            day = int(date[3:])
            return sum(months[:month - 1]) + day

        start = max(dayOfYear(arriveAlice), dayOfYear(arriveBob))
        end = min(dayOfYear(leaveAlice), dayOfYear(leaveBob))

        return max(0, end - start + 1)


