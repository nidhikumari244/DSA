class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """


        n = len(s)
        best = ""
        best_len = float('inf')
        
        for i in range(n):
            ones = 0
            for j in range(i, n):
                if s[j] == '1':
                    ones += 1
                if ones == k:
                    length = j - i + 1
                    candidate = s[i:j+1]
                    if length < best_len or (length == best_len and candidate < best):
                        best_len = length
                        best = candidate
                    break  # extending further only adds more 1's, no need to continue this i
        
        return best
