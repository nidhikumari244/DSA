class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        matched = 0

        # Match target prefix as much as possible
        while matched < len(s):
            idx = ord(target[matched]) - ord('a')

            if count[idx] == 0:
                break

            count[idx] -= 1
            matched += 1

        # If s itself can be rearranged exactly as target,
        # we still need a STRICTLY greater permutation
        for i in range(matched, -1, -1):

            if i < matched:
                # Put back the character used at position i
                idx = ord(target[i]) - ord('a')
                count[idx] += 1

            # Find the smallest available character > target[i]
            if i < len(s):
                target_idx = ord(target[i]) - ord('a')

                for j in range(target_idx + 1, 26):
                    if count[j] > 0:
                        # Choose this greater character
                        count[j] -= 1

                        answer = target[:i] + chr(j + ord('a'))

                        # Add remaining characters in sorted order
                        for k in range(26):
                            answer += chr(k + ord('a')) * count[k]

                        return answer

        return ""
