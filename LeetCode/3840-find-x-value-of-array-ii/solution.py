class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        m = 1
        while m < n:
            m <<= 1

        size = 2 * m
        tree_prod = [1] * size
        tree_M = [None] * size
        krange = range(k)

        def leaf_matrix(v):
            flat = [0] * (k * k)
            for a in krange:
                flat[a * k + (a * v) % k] = 1
            return flat

        zero_leaf = [0] * (k * k)

        for i in range(n):
            v = nums[i] % k
            tree_prod[m + i] = v
            tree_M[m + i] = leaf_matrix(v)
        for i in range(n, m):
            tree_prod[m + i] = 1 % k
            tree_M[m + i] = zero_leaf

        def pull(node):
            left = node << 1
            right = left | 1
            pl = tree_prod[left]
            tree_prod[node] = (pl * tree_prod[right]) % k
            ML, MR = tree_M[left], tree_M[right]
            M = [0] * (k * k)
            for a in krange:
                c = (a * pl) % k
                base_l, base_r = a * k, c * k
                for b in krange:
                    M[a * k + b] = ML[base_l + b] + MR[base_r + b]
            tree_M[node] = M

        for i in range(m - 1, 0, -1):
            pull(i)

        def update(idx, val):
            pos = m + idx
            v = val % k
            tree_prod[pos] = v
            tree_M[pos] = leaf_matrix(v)
            pos >>= 1
            while pos >= 1:
                pull(pos)
                pos >>= 1

        def query_suffix(start):
            l = start + m
            r = size
            left_nodes, right_nodes = [], []
            while l < r:
                if l & 1:
                    left_nodes.append(l)
                    l += 1
                if r & 1:
                    r -= 1
                    right_nodes.append(r)
                l >>= 1
                r >>= 1
            left_nodes.extend(reversed(right_nodes))

            cur = 1 % k
            vec_total = [0] * k
            for node in left_nodes:
                row = cur * k
                M = tree_M[node]
                for b in krange:
                    vec_total[b] += M[row + b]
                cur = (cur * tree_prod[node]) % k
            return vec_total

        result = []
        for index, value, start, x in queries:
            update(index, value)
            vec = query_suffix(start)
            result.append(vec[x])

        return result
