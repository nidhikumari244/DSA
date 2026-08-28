
class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        from collections import Counter
        n = len(s)
        cnt = Counter(s)
        odd_chars = [c for c in cnt if cnt[c] % 2 == 1]

        if n % 2 == 0:
            if len(odd_chars) != 0:
                return ""
            middle_char = ""
        else:
            if len(odd_chars) != 1:
                return ""
            middle_char = odd_chars[0]

        m = n // 2
        half_count = [0] * 26
        for c, v in cnt.items():
            half_count[ord(c) - ord('a')] = v // 2

        Th = target[:m]

        # Step 1: exact-match head case (best possible if it works)
        th_count = [0] * 26
        for c in Th:
            th_count[ord(c) - ord('a')] += 1
        if th_count == half_count:
            P = Th + middle_char + Th[::-1]
            if P > target:
                return P

        # Step 2: find the smallest head strictly greater than target[:m]
        counts_arr = half_count[:]
        best_H = None
        for i in range(m):
            tc_idx = ord(target[i]) - ord('a')
            found_idx = None
            for c_idx in range(tc_idx + 1, 26):
                if counts_arr[c_idx] > 0:
                    found_idx = c_idx
                    break
            if found_idx is not None:
                remaining = counts_arr[:]
                remaining[found_idx] -= 1
                suffix = ''.join(chr(idx + ord('a')) * remaining[idx] for idx in range(26))
                best_H = target[:i] + chr(found_idx + ord('a')) + suffix

            if counts_arr[tc_idx] > 0:
                counts_arr[tc_idx] -= 1
            else:
                break

        if best_H is not None:
            return best_H + middle_char + best_H[::-1]

        return ""
