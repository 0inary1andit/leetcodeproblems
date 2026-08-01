class Solution(object):
    def predictTheWinner(self, nums):
        
        n = len(nums)
    
    
  
        memo = [[None] * n for _ in range(n)]
    
  
        def Score(L, R):
      
            if memo[L][R] is not None:
                return memo[L][R]
            
  
            if L == R:
                return nums[L]
            
        
            pick_left = nums[L] - Score(L + 1, R)
            pick_right = nums[R] - Score(L, R - 1)
        
   
            memo[L][R] = max(pick_left, pick_right)
            return memo[L][R]

    
        return Score(0, n - 1) >= 0
        