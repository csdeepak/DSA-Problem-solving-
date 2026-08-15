class Solution(object):
    def maxSubArray(self, nums):
        sum1=0
        max1=0
        least=0
        for x in nums:
            least=min(sum1,x)
            sum1+=x
            
            if sum1<least:
                sum1=0
            max1=max(max1,sum1)
        return max1
            