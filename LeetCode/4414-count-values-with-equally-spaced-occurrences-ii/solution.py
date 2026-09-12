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
            if len (idx_list)<3:
                continue

            gap = idx_list[1]-idx_list[0]
            is_special=True
            for j in range(2,len(idx_list)):
                if idx_list[j]-idx_list[j-1] !=gap:
                    is_special = False
                    break

            if is_special:
                count+=1
        return count

        
        
