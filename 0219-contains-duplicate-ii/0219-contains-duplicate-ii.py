class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        
        n=len(nums)
        info=dict()
 
        for i in range(n):
            if nums[i] in info:
                if abs(i-info[nums[i]])<=k:
                    
                    return True 
                
                else:
                    info[nums[i]]=i    
            else:
                info[nums[i]]=i    
        return False  