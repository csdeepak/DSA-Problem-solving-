class Solution(object):
    def majorityElement(self, nums):
        me=nums[0]
        count=1
        for num in nums[1:]:
            if num==me:
                count+=1
            elif count==0:
                me=num
                count=1
            else:
                count-=1
        return me
        