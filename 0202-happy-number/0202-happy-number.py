class Solution(object):
    def isHappy(self, n):

        def sqrsum(num):
            sums=0
            while num!=0:
                rem=num%10
                sums+=rem*rem
                num=num//10

            return sums
        if n==1: return True
        p1=sqrsum(n)
        p2=sqrsum(sqrsum(n))
        while p2!=1:
            p2=sqrsum(sqrsum(p2))
            p1=sqrsum(p1)
            if p1==p2:
                return False

        return True        

        
        