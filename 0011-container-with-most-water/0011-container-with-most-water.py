class Solution(object):
    def maxArea(self, height):
        n=len(height)
        left=0
        right=n-1
        max_Area=0

        while left<right:
            area=(right-left)*min(height[left],height[right])
            max_Area=max(area,max_Area)
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1    


        return max_Area    
        