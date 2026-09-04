class Solution(object):
    def countSpecialIntegers(self, nums):
        seen = set()
        bad = set()

        prev = None

        for x in nums:
            if x != prev and x in seen:
                bad.add(x)

            seen.add(x)
            prev = x

        return len(seen) - len(bad)
