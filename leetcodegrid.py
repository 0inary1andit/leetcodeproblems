class Solution(object):
    def canPartitionGrid(self, grid): 
        m,n=len(grid),len(grid[0])
        total_sum=0

        for i in range (m):
            total_sum+=sum(grid[i])

            
       #horizontal cut 
        top_sum=0
        for i in range (m-1):
         top_sum+=sum(grid[i])
         if top_sum==total_sum-top_sum:
            return True


        left_sum=0
        for j in range(n-1):
         left_sum+=sum(grid[i][j] for i in range (m))
         if left_sum==total_sum-left_sum:
            return True
        
        return False




             
        


     
