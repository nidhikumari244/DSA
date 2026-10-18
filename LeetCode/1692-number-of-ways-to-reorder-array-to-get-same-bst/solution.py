class Solution(object):
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        comb = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            comb[i][0] = comb[i][i] = 1
            for j in range(1, i):
                comb[i][j] = (
                    comb[i - 1][j - 1] + comb[i - 1][j]
                ) % MOD

        def solver(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]

            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            ways_to_interleave = comb[len(arr) - 1][len(left)]

            left_ways = solver(left)
            right_ways = solver(right)

            return (
                ways_to_interleave * left_ways * right_ways
            ) % MOD

        return (solver(nums) - 1) % MOD


