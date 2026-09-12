class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        tri_k=[]
        tri_t=[]
        k=1
        t=1
        while t <=n:
            tri_k.append(k)
            tri_t.append(t)
            k+=1
            t=k*(k+1)//2
        D = [0] * (n + 1)
        for j in range(1, n + 1):
            best = float('inf')
            for idx in range(len(tri_t)):
                tk = tri_t[idx]
                if tk > j:
                    break
                cand = D[j - tk] + tri_k[idx] + 1   # +1 for the reset skip
                if cand < best:
                    best = cand
            D[j] = best
        ans = float('inf')
        for idx in range(len(tri_t)):
            tk = tri_t[idx]
            if tk <= n:
                cand = D[n - tk] + tri_k[idx]
                if cand < ans:
                    ans = cand
        return ans  
        
