class Solution(object):
    def maxProduct(self, nums):
        best=cur_min=cur_max=nums[0]
        for x in nums[1:]:
            candidate=(x,cur_min*x,cur_max*x)
            cur_min,cur_max=min(candidate),max(candidate)
            best=max(best,cur_max)
        return best 
        