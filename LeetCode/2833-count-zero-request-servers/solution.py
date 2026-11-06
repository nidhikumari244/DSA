class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        logs.sort(key=lambda l: l[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])

        cnt = [0] * (n + 1)
        active = 0
        left = right = 0
        m = len(logs)
        res = [0] * len(queries)

        for qi in order:
            q = queries[qi]
            # add logs with time <= q
            while right < m and logs[right][1] <= q:
                s = logs[right][0]
                if cnt[s] == 0:
                    active += 1
                cnt[s] += 1
                right += 1
            # remove logs with time < q - x
            while left < right and logs[left][1] < q - x:
                s = logs[left][0]
                cnt[s] -= 1
                if cnt[s] == 0:
                    active -= 1
                left += 1
            res[qi] = n - active
        return res
