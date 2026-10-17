# from typing import List
class Solution(object):
    def minSwaps(self, nums):
   

        def digit_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        n = len(nums)

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        position = {num: i for i, num in enumerate(nums)}

        swaps = 0

        for i in range(n):
            if nums[i] != sorted_nums[i]:
                swaps += 1

                j = position[sorted_nums[i]]

                position[nums[i]] = j
                position[nums[j]] = i

                nums[i], nums[j] = nums[j], nums[i]

        return swaps

        
