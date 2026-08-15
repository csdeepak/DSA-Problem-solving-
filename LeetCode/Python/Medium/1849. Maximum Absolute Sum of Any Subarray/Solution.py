class Solution(object):
    def maxAbsoluteSum(self, nums):
        cur_max=max_max=cur_min=min_min=nums[0]
        for x in nums[1:]:
            cur_max=max(x,cur_max+x)
            max_max=max(max_max,cur_max)
            cur_min=min(x,cur_min+x)
            min_min=min(cur_min,min_min)
        return max(-(min_min),max_max)