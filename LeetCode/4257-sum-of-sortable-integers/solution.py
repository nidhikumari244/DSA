class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        sorted_nums = sorted(nums)
        ans = 0

        def is_rotation(a, b):
            m = len(a)
            text = b + b

            lps = [0] * m
            j = 0

            for i in range(1, m):
                while j > 0 and a[i] != a[j]:
                    j = lps[j - 1]

                if a[i] == a[j]:
                    j += 1
                    lps[i] = j

            j = 0
            for value in text:
                while j > 0 and value != a[j]:
                    j = lps[j - 1]

                if value == a[j]:
                    j += 1

                if j == m:
                    return True

            return False

        for k in range(2, n + 1):
            if n % k != 0:
                continue

            possible = True

            for start in range(0, n, k):
                original = nums[start:start + k]
                target = sorted_nums[start:start + k]

                if not is_rotation(original, target):
                    possible = False
                    break

            if possible:
                ans += k

        # k = 1 is sortable only when nums is already sorted.
        if nums == sorted_nums:
            ans += 1

        return ans


