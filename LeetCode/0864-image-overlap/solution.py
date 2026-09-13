class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        if not ones1 or not ones2:
            return 0
        
        overlap_count = {}
        best = 0
        
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift = (r1 - r2, c1 - c2)
                overlap_count[shift] = overlap_count.get(shift, 0) + 1
                best = max(best, overlap_count[shift])
        
        return best
