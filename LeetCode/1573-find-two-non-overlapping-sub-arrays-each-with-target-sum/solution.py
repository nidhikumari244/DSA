class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        INF = float('inf')
        
        # best_end[i] = length of the shortest valid subarray ending at or before index i
        best_end = [INF] * n
        
        left = 0
        window_sum = 0
        best_so_far = INF
        result = INF
        
        for right in range(n):
            window_sum += arr[right]
            
            while window_sum > target:
                window_sum -= arr[left]
                left += 1
            
            if window_sum == target:
                curr_len = right - left + 1
                # If there's a valid earlier subarray ending before this one starts,
                # combine them.
                if left > 0 and best_end[left - 1] != INF:
                    result = min(result, best_end[left - 1] + curr_len)
                best_so_far = min(best_so_far, curr_len)
            
            best_end[right] = best_so_far
        
        return result if result != INF else -1
