class Solution:
    
    def countWhileMergeSort(self, left, right):
        # Single element edge case
        if left == right:
            return 0
        # Divide and conquer step
        # Note: left and right are inclusive
        mid = (left + right)//2
        count = self.countWhileMergeSort(left, mid) + self.countWhileMergeSort(mid+1,right)
        #print(left, mid, right, count)
        # Merge step
        # j is the index to find where in the right sorted subarray that satisfies the reverse pair conditions
        # t is the index for conducting merge sort
        # t begins at mid+1 because [left,right] are both inclusive
        # in this problem, j should start from the end as the nums are sorted, 
        j = t = mid + 1
        # temp array to carry out merge sort
        cache = [0]*(right-left+1)
        p = 0  # p is pointer to current cache item
        for i in range(left, mid + 1):
            # j is the first index satisfy nums[i] > 2*nums[j]
            while j <= right and 2*self.nums[j] < self.nums[i]:
                j += 1
            #print("i = ", i, "j = ", j)
            # t is for copying to temp array for merge sort
            # In this step, are the sums[t] smaller than sums[i] are put into the temp array before sums[i]
            while t <= right and self.nums[t] < self.nums[i] :
                cache[p] = self.nums[t]
                p += 1
                t += 1
            cache[p] = self.nums[i]
            p += 1
            count += j - (mid+1)
        self.nums[left:t]=cache[:p]
        #print(self.nums, left, right, count)
        return count
    
    def reversePairs(self, nums: List[int]) -> int:
        self.nums = nums
        return self.countWhileMergeSort(0, len(nums)-1)
        
        
    
        