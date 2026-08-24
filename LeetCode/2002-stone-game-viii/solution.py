class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """


        
        # Calculate prefix sums
        for i in range(1, len(stones)):
            stones[i] += stones[i - 1]
        
        # Initially, taking all stones
        dp = stones[-1]
        
        # Work backwards
        for i in range(len(stones) - 2, 0, -1):
            dp = max(dp, stones[i] - dp)
        
        return dp
        
