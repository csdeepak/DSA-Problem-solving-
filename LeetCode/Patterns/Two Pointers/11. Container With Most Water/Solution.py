class Solution(object):
    def maxArea(self, height):
        length =breadth =0
        area=0
        high, low=len(height)-1, 0
        while high>low:
            breadth=high-low
            if height[high]<height[low]:
                length=height[high]
                high-=1
            else:
                length=height[low]
                low+=1
            area=max(area,length*breadth)
            
        return area 