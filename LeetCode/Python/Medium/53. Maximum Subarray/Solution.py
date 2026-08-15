class Solution(object):
    def maxSubArray(self, nums):
        sum1=0
        max1=0
        su
        for x in nums:
            sum1+=x
            if sum1<0:
                sum1=0
            max1=max(max1,sum1)
        return max1
            