class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """

        min_odd = float('inf')
        min_even = float('inf')

        for num in nums1:
            if num % 2 == 0:
                min_even = min(min_even, num)
            else:
                min_odd = min(min_odd, num)

        # All numbers are already even
        if min_odd == float('inf'):
            return True

        # Make everything odd
        return min_odd < min_even
