class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = 0

        for i in range(len(s)):
            position = ord(s[i]) - ord('a') + 1
            reverse_position = 27 - position

            ans += reverse_position * (i + 1)

        return ans
        
