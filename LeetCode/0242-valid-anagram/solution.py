class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq_s={}
        for i in range (0,len(s)):
            if s[i] in freq_s:
                freq_s[s[i]]= freq_s[s[i]] +1
            else :
                freq_s[s[i]] =1

        freq_t={}
        for i in range (0,len(t)):
            if t[i] in freq_t:
                freq_t[t[i]]= freq_t[t[i]] +1
            else:
                freq_t[t[i]] =1 

        if len(s) != len(t):
            return False 

        if freq_s != freq_t:
            return False 
        return True 

