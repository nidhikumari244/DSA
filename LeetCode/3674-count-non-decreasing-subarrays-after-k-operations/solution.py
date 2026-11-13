from collections import deque

class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        b = nums[::-1]
        dq = deque()      # indices, values strictly decreasing
        S = 0             # sum of suffix maxes over window [l..r]
        win_sum = 0       # sum of elements in window
        l = 0
        ans = 0

        for r, x in enumerate(b):
            # add b[r]
            win_sum += x
            while dq and b[dq[-1]] <= x:
                j = dq.pop()
                prev = dq[-1] if dq else l - 1
                S -= b[j] * (j - prev)
            prev = dq[-1] if dq else l - 1
            S += x * (r - prev)
            dq.append(r)

            # shrink while cost exceeds k
            while S - win_sum > k:
                S -= b[dq[0]]        # suffix max at position l
                win_sum -= b[l]
                if dq[0] == l:
                    dq.popleft()
                l += 1

            ans += r - l + 1

        return ans
