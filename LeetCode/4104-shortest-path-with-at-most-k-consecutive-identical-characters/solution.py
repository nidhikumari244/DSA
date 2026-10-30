class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        import heapq


        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        INF = float('inf')
        minrun = [k + 1] * n          # smallest run already finalized at each node
        heap = [(0, 0, 1)]            # (dist, node, run)

        while heap:
            d, u, r = heapq.heappop(heap)
            if r >= minrun[u]:
                continue              # dominated by an earlier, cheaper-or-equal state
            minrun[u] = r
            if u == n - 1:
                return d
            lu = labels[u]
            for v, w in adj[u]:
                nr = r + 1 if labels[v] == lu else 1
                if nr > k or nr >= minrun[v]:
                    continue
                heapq.heappush(heap, (d + w, v, nr))

        return -1
