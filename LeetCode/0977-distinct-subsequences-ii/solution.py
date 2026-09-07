class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """

        MOD = 10**9 + 7

        dp = 1
        last = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')

            new_dp = (2 * dp - last[idx]) % MOD

            last[idx] = dp
            dp = new_dp

        return (dp - 1) % MOD
        
