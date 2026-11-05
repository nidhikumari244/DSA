class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        m=len(arr2)
        count=0
        for x in arr1:
            i=bisect_left(arr2,x-d)
            if i == m or arr2[i] > x + d:
                count +=1
        return count 
