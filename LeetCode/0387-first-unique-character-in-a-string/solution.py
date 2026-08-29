class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}

        # Count frequency of every character
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Find the first non-repeating character
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1
