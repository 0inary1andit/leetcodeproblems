class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def divisor(x):
            dsum=0
            prod=1
            while x!=0:
                rem=x%10
                dsum+=rem
                prod*=rem
                x=x//10

            return dsum+prod 

        p=divisor(n)
        if n%p==0:
            return True
        else:
            return False

        