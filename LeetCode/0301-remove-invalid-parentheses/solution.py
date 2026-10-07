from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(string):
            balance = 0
            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0
        
        if isValid(s):
            return [s]
        
        visited = {s}
        queue = deque([s])
        result = []
        found = False
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                current = queue.popleft()
                
                if isValid(current):
                    result.append(current)
                    found = True
                
                if found:
                    continue  # don't bother generating next level if we already found answers at this level
                
                for i in range(len(current)):
                    if current[i] not in '()':
                        continue
                    next_str = current[:i] + current[i+1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append(next_str)
            
            if found:
                break
        
        return result
