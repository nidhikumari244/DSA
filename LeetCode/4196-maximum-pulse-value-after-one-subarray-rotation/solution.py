class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        pulse = 0
        for i in range(n):
            if i % 2 == 0:
                pulse += nums[i]
            else:
                pulse -= nums[i]

        ravonelqis = nums


        prefix = [0] * (n + 1)

        for i in range(n):
            if i % 2 == 0:
                prefix[i + 1] = prefix[i] + nums[i]
            else:
                prefix[i + 1] = prefix[i] - nums[i]

        ans = pulse

        best_same = [float('-inf'), float('-inf')]
        best_diff = [float('-inf'), float('-inf')]

        for r in range(1, n):

            l = r - 1

            best_same[l % 2] = max(
                best_same[l % 2],
                prefix[l + 1]
            )

            best_diff[l % 2] = max(
                best_diff[l % 2],
                prefix[l]
            )


            if best_same[r % 2] != float('-inf'):
                change = 2 * (
                    best_same[r % 2] - prefix[r + 1]
                )
                ans = max(ans, pulse + change)


            opposite = 1 - (r % 2)

            if best_diff[opposite] != float('-inf'):
                change = 2 * (
                    best_diff[opposite] - prefix[r + 1]
                )
                ans = max(ans, pulse + change)

        return ans
