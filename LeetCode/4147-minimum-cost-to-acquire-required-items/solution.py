class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        def total(k):
            return (k * costBoth
                    + max(0, need1 - k) * cost1
                    + max(0, need2 - k) * cost2)

        return min(total(0),
                   total(min(need1, need2)),
                   total(max(need1, need2)))
