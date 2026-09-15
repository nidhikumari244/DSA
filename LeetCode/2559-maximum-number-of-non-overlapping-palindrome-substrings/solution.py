class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        n = len(s)
        if n < k:
            return 0
        
        # isPal[i][j] = True if s[i..j] is a palindrome
        isPal = [[False] * n for _ in range(n)]
        for i in range(n):
            isPal[i][i] = True
        for i in range(n - 1):
            isPal[i][i + 1] = (s[i] == s[i + 1])
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                isPal[i][j] = (s[i] == s[j]) and isPal[i + 1][j - 1]
        
        count = 0
        i = 0
        while i <= n - k:
            if isPal[i][i + k - 1]:
                count += 1
                i += k
            elif i + k <= n - 1 and isPal[i][i + k]:
                count += 1
                i += k + 1
            else:
                i += 1
        
        return count
