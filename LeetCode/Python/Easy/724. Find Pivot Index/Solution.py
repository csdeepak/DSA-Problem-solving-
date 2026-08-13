class Solution(object):
    def pivotIndex(self, nums):
        current=0 
        for i in range(len(nums)):   
            current+=nums[i]
            nums[i]=current
           
        for i in range(0,len(nums)):
            left = 0 if i == 0 else nums[i - 1]
            if left==nums[len(nums)-1]-nums[i]:
                i
                return i

        return -1
               

        

        

    

        
        