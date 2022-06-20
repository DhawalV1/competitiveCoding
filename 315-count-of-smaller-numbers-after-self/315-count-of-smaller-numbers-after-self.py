class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        bucket_size = 100
        nums = [n+10000 for n in nums]
        max_n = max(nums)
        max_buckets = 1 + (max_n // bucket_size)
        
        bucket_count = [0 for _ in range(max_buckets)]
        counts = [0 for _ in range(max_n + 1)]

        ans_arr = []
        for n in reversed(nums):
            j = n // bucket_size
            ans = sum(bucket_count[:j]) + sum(counts[bucket_size*j:n])
            ans_arr.append(ans)
            counts[n] += 1
            bucket_count[j] += 1
        
        return reversed(ans_arr)
        