import bisect

class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)
        
        # Sort original indices by right endpoint ascending
        order = sorted(range(n), key=lambda i: intervals[i][1])
        rs = [intervals[i][1] for i in order]  # sorted r-values
        
        # dp[p][k] = (best_score, best_sorted_index_list) using the first p
        # intervals (in r-sorted order), choosing at most k of them.
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for p in range(1, n + 1):
            idx = order[p - 1]
            l, r, w = intervals[idx]
            # All compatible predecessors (r < l) are exactly the elements
            # before this one in r-sorted order, since rs is sorted ascending.
            bound = bisect.bisect_left(rs, l)
            
            for k in range(5):
                best_score, best_list = dp[p - 1][k]          # skip this interval
                if k >= 1:
                    sub_score, sub_list = dp[bound][k - 1]
                    cand_score = sub_score + w
                    cand_list = sorted(sub_list + [idx])       # take this interval
                    if cand_score > best_score or (cand_score == best_score and cand_list < best_list):
                        best_score, best_list = cand_score, cand_list
                dp[p][k] = (best_score, best_list)
        
        return dp[n][4][1]
