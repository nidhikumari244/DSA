class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """


        current = 0
        maximum = 0

        for ch in s:
            if ch == '(':
                current += 1
                maximum = max(maximum, current)

            elif ch == ')':
                current -= 1

        return maximum
        
