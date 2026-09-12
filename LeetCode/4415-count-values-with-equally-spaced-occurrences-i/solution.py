class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        indices={}
        for i , num in enumerate(nums):
            indices.setdefault(num,[]).append(i)
        count=0
        for num , idx_list in indices.items():
            if len (idx_list)==3:
                i1,i2,i3=idx_list
                if i2-i1==i3-i2:
                    count +=1
        return count
        
