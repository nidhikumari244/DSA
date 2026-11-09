class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """

        count = [0] * k

        # free servers, stored as virtual slot numbers (slot % k == server id)
        free = list(range(k))
        heapq.heapify(free)

        # busy servers as (end_time, virtual_slot)
        busy = []

        for i in range(len(arrival)):
            t = arrival[i]

            # release servers that have finished by time t
            while busy and busy[0][0] <= t:
                _, slot = heapq.heappop(busy)
                sid = slot % k
                # re-place this server at its next virtual slot at or after i
                heapq.heappush(free, i + ((sid - i) % k))

            if not free:
                continue  # all servers busy, drop request

            slot = heapq.heappop(free)
            sid = slot % k
            count[sid] += 1
            heapq.heappush(busy, (t + load[i], slot))

        best = max(count)
        return [i for i in range(k) if count[i] == best]
