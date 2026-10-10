class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """

 


        k = k1 + k2
        n = len(nums1)
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diffs) <= k:
            return 0

        mx = max(diffs)
        cnt = [0] * (mx + 2)
        for d in diffs:
            cnt[d] += 1

        c = 0
        v = mx
        while v > 0:
            c += cnt[v]
            if c == 0:
                v -= 1
                continue
            if k >= c:
                k -= c
                v -= 1
                cnt[v] += 0  
            else:
                break
        else:
            return 0

        res = k * (v - 1) ** 2 + (c - k) * v ** 2

        for val in range(1, v):
            res += cnt[val] * val * val

        return res
