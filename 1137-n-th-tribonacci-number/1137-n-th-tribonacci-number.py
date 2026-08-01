class Solution(object):
    def tribonacci(self, n):
       
        value={}
        

        def trib(n):
     
            if n in value: return value[n]
            if(n==0): return 0
            if(n<=2): return 1
            else:
                result=trib(n-1)+trib(n-2)+trib(n-3)
                value[n]=result

            return result    
         
    
    
        return trib(n)
    
