class Solution(object):
    def scoreOfParentheses(self, s):
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                current = stack.pop()

                if current == 0:
                    current = 1
                else:
                    current = 2 * current

                stack[-1] += current

        return stack[0]
