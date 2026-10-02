class Solution(object):
    def longestCommonPrefix(self, strs):

        # if not strs:
        #     return ""
        
        # for i in range(len(strs[0])):
        #     char = strs[0][i]
        #     for s in strs[1:]:
        #         if i >= len(s) or s[i] != char:
        #             return strs[0][:i]
        
        # return strs[0]

        ans=""
        sortest_str= min(len(x) for x in strs )
        for i in range( 0, sortest_str):
            mismatch = False
            for j in range (0, len(strs)):
                if strs [j][i] != strs[0][i]:
                    mismatch = True 
                    break
            if mismatch:
                break 
            else :
                ans = ans+ strs[0][i]
        return ans 


        
