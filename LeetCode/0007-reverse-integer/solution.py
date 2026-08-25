class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev=0
        if x<0:
            negative= True
            x=abs(x)
        else:
            negative=False
        while x != 0:
            digit = x % 10
            x = x // 10
            if negative :
                limit_digit=8
            else:
                limit_digit=7
            if rev > 214748364 or rev == 214748364 and digit > limit_digit:
                return 0
            rev= rev*10+digit
        if negative:
            
            rev= -rev
           
        
        return rev

        
        
