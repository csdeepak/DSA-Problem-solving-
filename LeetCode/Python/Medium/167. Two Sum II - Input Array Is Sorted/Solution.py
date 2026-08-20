class Solution(object):
    def twoSum(self, numbers, target):
        lo,hi=0,len(numbers)-1
        while(lo<hi):
            s=numbers[lo]+numbers[hi]
            if s==target:
                return [lo+1,hi+1]
            elif s< target:
                lo+=1
            else:
                hi-=1
