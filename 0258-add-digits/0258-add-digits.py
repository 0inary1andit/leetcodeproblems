class Solution(object):
    def addDigits(self, num):
        def add(x):
            sum=0
            while x!=0:
                r=x%10
                sum+=r
                x=x//10

            return sum
        
        digits=[0,1,2,3,4,5,6,7,8,9]

        final_sum=num
        while final_sum not in digits:
            final_sum=add(num)
            num=final_sum
        
        

     

        return final_sum