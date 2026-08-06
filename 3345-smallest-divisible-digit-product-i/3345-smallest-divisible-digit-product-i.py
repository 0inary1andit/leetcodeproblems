class Solution(object):
    def smallestNumber(self, n, t):
        def pod(x):
            prod=1
            while x!=0:
                a=x%10
                prod*=a
                x=x//10

            return prod

        for i in range(n,n+10):
            curr=pod(i)
            if curr%t==0:
                return i
        
        