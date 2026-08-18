from collections import Counter

class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
       
        if k == n:
            return max(nums)
            
   
        count = Counter(nums)
        
        
        if k == 1:
            ans = -1
            for num, freq in count.items():
                if freq == 1:
                    ans = max(ans, num)
            return ans
            
   
        ans = -1
        if count[nums[0]] == 1:
            ans = max(ans, nums[0])
            
        if count[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans