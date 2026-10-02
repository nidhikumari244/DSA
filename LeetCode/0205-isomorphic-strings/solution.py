class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping_st={}
        mapping_ts={}
        for i in range (0,len(s)):
            current_s=s[i]
            current_t=t[i]

            if current_s in mapping_st:
                if mapping_st[current_s]!= current_t:
                    return False
            if current_t in mapping_ts:
                if mapping_ts[current_t]!=current_s:
                    return False
            mapping_st[current_s] = current_t
            mapping_ts[current_t] = current_s
        return True 
        
