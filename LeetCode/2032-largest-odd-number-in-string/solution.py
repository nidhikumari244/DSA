class Solution(object):
    def largestOddNumber(self, s):
        """
        :type num: str
        :rtype: str
        """
        odd_index=-1
        for i in range (len(s) -1,-1,-1):
            if int(s[i])% 2 != 0:
                odd_index=i
                break
        ans=""
        for i in range (0,odd_index+1):
            ans=ans+s[i]
        result=""

        found_non_zero=False
        for i in range(len(ans)):
            if found_non_zero==False and ans[i]=="0":
                continue
            found_non_zero=True
            result = result + ans[i]
        return result 

            
