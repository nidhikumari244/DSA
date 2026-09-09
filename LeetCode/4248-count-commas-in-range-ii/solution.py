class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """

        ans = 0
        power = 1000
        commas = 1

        while power <= n:
            end = min(n, power * 1000 - 1)
            ans += (end - power + 1) * commas

            power *= 1000
            commas += 1

        return ans
        
