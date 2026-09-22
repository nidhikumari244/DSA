class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0

        is_prime = bytearray([1]) * n
        is_prime[0] = 0
        is_prime[1] = 0

        # eliminate all even numbers >= 4 in one bulk slice (2 stays prime)
        is_prime[4:n:2] = bytearray(len(range(4, n, 2)))

        # only need to sieve with odd i now
        for i in range(3, int(n ** 0.5) + 1, 2):
            if is_prime[i]:
                is_prime[i*i:n:2*i] = bytearray(len(range(i*i, n, 2*i)))

        return sum(is_prime)
