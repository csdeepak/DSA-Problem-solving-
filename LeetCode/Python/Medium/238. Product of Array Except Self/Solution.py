class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        result=[1]*n
        
        prefix=1
        for i in range(n):
            result[i]=prefix
            prefix*=nums[i]
            
        sufix=1
        for i in range(n-1,-1,-1):
            result[i]*=sufix
            sufix*=nums[i]

        return result
