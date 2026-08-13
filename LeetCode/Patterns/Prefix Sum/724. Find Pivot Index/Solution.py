class Solution(object):
    def pivotIndex(self, nums):
        current=0 
        for i in range(len(nums)):   
            current+=nums[i]
            nums[i]=current
        n=0   
        for i in range(0,len(nums)):
            left = 0 if i == 0 else nums[i - 1]
            if left==nums[len(nums)-1]-nums[i]:
                n=i
                break
            else :
                n=i
        if n==(len(nums)-1):
            return -1
        else:
            return n
               

        

        

    

        
        