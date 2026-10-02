class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len (s) != len(goal):
            return False 
        sum_s= s+s
        for i in range (0,len(s)):
            if sum_s[i:i+len(s)] == goal:
                return True 
        return False 
