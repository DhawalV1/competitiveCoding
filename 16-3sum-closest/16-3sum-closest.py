class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3: return
        sub_closest_dist = sys.maxsize
        closest = 0
        nums.sort()
        for i in range(len(nums)-2):
          l = i + 1; r = len(nums) - 1
          sub_target = target - nums[i]
          while l < r:
            s = nums[l] + nums[r]
            if abs(s - sub_target) < sub_closest_dist:
              sub_closest_dist = abs(s - sub_target)
              closest = s + nums[i]
            if s > sub_target:
              r -= 1
            else:
              l += 1
        return closest