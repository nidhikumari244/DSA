class Solution(object):
    def minOperations(self, nums, sum):
        INF = float('inf')

        # dp[s] = minimum operations needed to make sum s
        dp = [INF] * (sum + 1)
        dp[0] = 0

        for num in nums:

            # value -> minimum operations to obtain this value
            options = {}

            # -------------------------
            # Divide: num -> num//2 ...
            # -------------------------
            x = num
            cost = 0

            while x > 0:
                if x <= sum:
                    options[x] = min(options.get(x, INF), cost)

                x //= 2
                cost += 1

            # -------------------------
            # Multiply: num -> num*2 ...
            # -------------------------
            x = num
            cost = 0

            while x <= sum:
                options[x] = min(options.get(x, INF), cost)

                x *= 2
                cost += 1

            # -------------------------
            # 0/1 Knapsack
            # -------------------------
            new_dp = dp[:]

            for value, cost in options.items():

                for s in range(sum - value + 1):

                    if dp[s] != INF:
                        new_dp[s + value] = min(
                            new_dp[s + value],
                            dp[s] + cost
                        )

            dp = new_dp

        return -1 if dp[sum] == INF else dp[sum]
