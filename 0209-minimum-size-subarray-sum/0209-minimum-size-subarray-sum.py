class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)


        curr_sum=0
        left=0
        min_len=float('inf')

        for i in range(n):
            curr_sum+=nums[i]
            while(curr_sum>=target):
                min_len=min(min_len,i-left+1)
                curr_sum-=nums[left]
                left=left+1

            
        
        return min_len if min_len != float('inf') else 0

        