class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = 0
        need = 0

        for ch in s:
            if ch == '(':
                if need % 2 == 1:
                    ans += 1
                    need -= 1

                need += 2

            else:
                need -= 1

                if need < 0:
                    ans += 1
                    need = 1

        return ans + need
