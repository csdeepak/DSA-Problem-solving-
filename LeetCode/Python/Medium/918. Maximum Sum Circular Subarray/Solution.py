class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total=sum(nums)
        cur_max=max_max=cur_min=min_min=nums[0]
        for x in nums[1:]:
            cur_max=max(x,cur_max+x)
            max_max=max(cur_max,max_max)
            cur_min=min(x,cur_min+x)
            min_min=min(min_min,cur_min)

        if max_max <0:
                return max_max
        return max(total-min_min,max_max)