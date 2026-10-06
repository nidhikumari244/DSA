
class Solution(object):
    def minAddToMakeValid(self, s):
        open = 0
        add = 0

        for ch in s:
            if ch == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    add += 1

        return add + open


