class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        i, j = min(min_idx, max_idx), max(min_idx, max_idx)
        
        # Option 1: remove both from the front (up through the later index)
        from_front = j + 1
        # Option 2: remove both from the back (from the earlier index onward)
        from_back = n - i
        # Option 3: remove earlier one from front, later one from back
        both_ends = (i + 1) + (n - j)
        
        return min(from_front, from_back, both_ends)
