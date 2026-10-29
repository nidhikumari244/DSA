class Solution:
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # DFS order, parent, depth
        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        order = []

        stack = [0]
        parent[0] = 0
        while stack:
            u = stack.pop()
            tin[u] = len(order)
            order.append(u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)

        # Subtree sizes -> Euler tour exit times
        size = [1] * n
        for u in reversed(order):
            if u != 0:
                size[parent[u]] += size[u]
        tout = [tin[u] + size[u] - 1 for u in range(n)]

        # Binary lifting for LCA
        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        for u in range(n):
            up[0][u] = parent[u]
        for k in range(1, LOG):
            for u in range(n):
                up[k][u] = up[k - 1][up[k - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = up[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return parent[u]

        def get_bit(c):
            return 1 << (ord(c) - 97)

        # Root-to-node prefix XOR of character masks
        prefix = [0] * n
        for u in order:
            prefix[u] = get_bit(s[u])
            if u != 0:
                prefix[u] ^= prefix[parent[u]]

        # Fenwick tree: range XOR update, point query
        bit = [0] * (n + 2)

        def add(i, value):
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def point_query(i):
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        def range_update(l, r, value):
            add(l + 1, value)
            if r + 2 <= n:
                add(r + 2, value)

        def get_prefix(u):
            return prefix[u] ^ point_query(tin[u] + 1)

        result = []
        s = list(s)

        for query in queries:
            parts = query.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                delta = get_bit(s[u]) ^ get_bit(c)
                if delta:
                    range_update(tin[u], tout[u], delta)
                    s[u] = c
            else:
                u = int(parts[1])
                v = int(parts[2])
                a = lca(u, v)
                mask = get_prefix(u) ^ get_prefix(v) ^ get_bit(s[a])
                result.append(mask & (mask - 1) == 0)

        return result
