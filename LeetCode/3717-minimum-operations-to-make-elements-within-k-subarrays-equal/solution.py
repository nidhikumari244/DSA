class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        vals = sorted(set(nums))
        idx = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)
        LOG = m.bit_length()

        def update(i, c, s):
            while i <= m:
                cnt[i] += c
                sm[i] += s
                i += i & -i

        def query(i):
            c = s = 0
            while i > 0:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s

        def kth(kk):  # smallest compressed index whose prefix count >= kk
            pos = 0
            for b in range(LOG, -1, -1):
                np_ = pos + (1 << b)
                if np_ <= m and cnt[np_] < kk:
                    pos = np_
                    kk -= cnt[np_]
            return pos + 1

        # cost[s] = cost to make nums[s:s+x] equal
        cost = [0] * (n - x + 1)
        total = 0
        for i in range(n):
            update(idx[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                update(idx[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                p = kth(x // 2 + 1)
                med = vals[p - 1]
                c_le, s_le = query(p)
                cost[i - x + 1] = (med * c_le - s_le) + ((total - s_le) - med * (x - c_le))

        INF = float('inf')
        prev = [0] * (n + 1)  # j = 0 subarrays
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(j * x, n + 1):
                cur[i] = min(cur[i - 1], prev[i - x] + cost[i - x])
            prev = cur
        return prev[n]
