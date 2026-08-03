class Solution(object):
    def climbStairs(self, n):
        memory={}
        def recur(n):

            if(n<=2):return n
            else:
                if(n in memory):
                    return memory[n]

                else:
                    result=recur(n-1)+recur(n-2)
                    memory[n]=result
                    return result   


        return recur(n)

       
        