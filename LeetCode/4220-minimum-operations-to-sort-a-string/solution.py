class Solution(object):
    def minOperations(self, s):
        n = len(s)
        if s == ''.join(sorted(s)):
            return 0
        if n == 2:
            return -1

        mn, mx = min(s), max(s)
        if s[0] == mn or s[-1] == mx:
            return 1

        # max only at the front and min only at the back -> 3
        if s.count(mx) == 1 and s[0] == mx and s.count(mn) == 1 and s[-1] == mn:
            return 3

        return 2
