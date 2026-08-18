from collections import Counter

class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        # Case 1: The only subarray is the array itself
        if k == n:
            return max(nums)
            
        # Count global frequencies of all elements
        count = Counter(nums)
        
        # Case 2: Subarrays are size 1, so elements must be globally unique
        if k == 1:
            ans = -1
            for num, freq in count.items():
                if freq == 1:
                    ans = max(ans, num)
            return ans
            
        # Case 3: 1 < k < n 
        # Only the absolute bounds (first and last elements) can belong to exactly 1 subarray
        ans = -1
        if count[nums[0]] == 1:
            ans = max(ans, nums[0])
            
        if count[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans