class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """

        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        
        
        x_overlap = min(x2, x4) - max(x1, x3)
        y_overlap = min(y2, y4) - max(y1, y3)
        
        return x_overlap > 0 and y_overlap > 0
