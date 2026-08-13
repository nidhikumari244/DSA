class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n= len(nums)
        if n<2:
            return 0
        min_num=min(nums)
        max_num=max(nums)

        if min_num == max_num:
            return 0

        bucket_count=n-1
        bucket_size=(max_num - min_num + bucket_count -1)// bucket_count

        bucket_min=[float('inf')]*bucket_count
        bucket_max=[float('-inf')]*bucket_count



        for num in nums:
            if num==min_num or num==max_num:
                continue
            bucket_index=(num-min_num)//bucket_size
            if num<bucket_min[bucket_index]:
                bucket_min[bucket_index]=num
            if num>bucket_max[bucket_index]:
                bucket_max[bucket_index]=num



        
        max_gap=0
        previous_max=min_num

        for i in range(bucket_count):
            if bucket_min[i]==float('inf'):
                continue

            gap=bucket_min[i]-previous_max
            if gap>max_gap:
                max_gap=gap
            previous_max=bucket_max[i]
            
        gap = max_num-previous_max
        if gap > max_gap:
            max_gap = gap 
        return max_gap       
        
