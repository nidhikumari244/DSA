class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        n = len(nums)
        best = 0
        
        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                l = l * nums[j] // gcd(l, nums[j])
                
                if prod == l * g:
                    best = max(best, j - i + 1)
        
        return best
