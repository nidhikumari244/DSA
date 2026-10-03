class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq={}
        for i in range ( 0, len(s)):
            if s[i] in freq:
                freq[s[i]]= freq[s[i]] + 1
            else:
                freq[s[i]]=1
        sort_chr= sorted(freq.keys(), key=lambda x: (-freq[x],x))

        ans=""

        for x in sort_chr:
            ans=ans+x*freq[x]

        return ans 

        
        
