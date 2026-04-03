#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#Find two lines that together with the x-axis form a container, such that the container contains the most water.
#Return the maximum amount of water a container can store.
#Notice that you may not slant the container.

#bruteforce
def maxArea(height):
    n=len(height)
    res=0
    
    for l in range(n):
        for r in range(l+1,n):
            area=(r-l)*min(height[l],height[r])
            res=max(res,area)
            
            
    return res        

#optimized

def maxArea(height):
    n=len(height)
    res=0
    r=n-1
    l=0
    
    while l<r:
        area=(r-l)*min(height[l],height[r])
        res=max(res,area)
        if height[l]<height[r]:
            l+=1
        else:
            r-=1    
            
        
    return max    
        