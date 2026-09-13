class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def palistr(left,right):
            if left>=right:
                return True
            if not s[left].isalnum():
                return palistr( left + 1, right)
            if not s[right].isalnum():
                return palistr( left, right - 1)

            if s[left].lower() !=s[right].lower():
                return False
            return palistr(left+1,right-1)
        return palistr (0,len(s)-1)
        
