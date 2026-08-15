class Solution(object):
    def maxSubArray(self, nums):
        sum1 = nums[0]
        max1 = nums[0]

        for x in nums[1:]:
            sum1 = max(x, sum1 + x)
            max1 = max(max1, sum1)

        return max1