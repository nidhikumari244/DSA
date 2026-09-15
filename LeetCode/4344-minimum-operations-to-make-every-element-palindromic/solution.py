class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        total = 0
        for n in nums:
            v = cache.get(n)
            if v is None:
                v = self._min_ops_for(n)
                cache[n] = v
            total += v
        return total

    def _min_ops_for(self, n):
        s = str(n)
        L = len(s)
        parity = n % 2
        allowed = (2, 4, 6, 8) if parity == 0 else (1, 3, 5, 7, 9)
        best = None

        # ---- same-length candidates: pal is monotonic in h, so only the
        # allowed leading digit(s) nearest n's own leading digit can matter ----
        k = (L + 1) // 2
        even_len = (L % 2 == 0)
        prefix = int(s[:k])
        d0 = int(s[0])

        lower_d = None
        upper_d = None
        for d in allowed:
            if d <= d0 and (lower_d is None or d > lower_d):
                lower_d = d
            if d >= d0 and (upper_d is None or d < upper_d):
                upper_d = d

        cand_ds = []
        if lower_d is not None:
            cand_ds.append(lower_d)
        if upper_d is not None and upper_d != lower_d:
            cand_ds.append(upper_d)

        for d in cand_ds:
            if k == 1:
                lo = hi = d
            else:
                lo = d * (10 ** (k - 1))
                hi = lo + (10 ** (k - 1)) - 1
            for h_try in (prefix - 1, prefix, prefix + 1):
                h = h_try
                if h < lo:
                    h = lo
                elif h > hi:
                    h = hi
                hs = str(h)
                if even_len:
                    pal = int(hs + hs[::-1])
                else:
                    pal = int(hs + hs[:-1][::-1])
                diff = n - pal if n > pal else pal - n
                if best is None or diff < best:
                    best = diff

        # ---- shorter length L-1: max palindrome of that length always
        # comes from the largest allowed leading digit ----
        if L - 1 >= 1:
            Lc = L - 1
            k2 = (Lc + 1) // 2
            d = allowed[-1]  # allowed is sorted ascending
            if k2 == 1:
                h = d
            else:
                lo2 = d * (10 ** (k2 - 1))
                h = lo2 + (10 ** (k2 - 1)) - 1
            hs = str(h)
            if Lc % 2 == 0:
                pal = int(hs + hs[::-1])
            else:
                pal = int(hs + hs[:-1][::-1])
            diff = n - pal if n > pal else pal - n
            if diff < best:
                best = diff

        # ---- longer length L+1: min palindrome of that length always
        # comes from the smallest allowed leading digit ----
        Lc = L + 1
        k2 = (Lc + 1) // 2
        d = allowed[0]
        if k2 == 1:
            h = d
        else:
            h = d * (10 ** (k2 - 1))
        hs = str(h)
        if Lc % 2 == 0:
            pal = int(hs + hs[::-1])
        else:
            pal = int(hs + hs[:-1][::-1])
        diff = n - pal if n > pal else pal - n
        if diff < best:
            best = diff

        return best // 2
