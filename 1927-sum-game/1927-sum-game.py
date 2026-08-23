class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n=len(num)
        diff_sum=0
        diff_count=0

        for i in range(n):
            if i<n//2:
                if num[i]=="?":
                    diff_count+=1
                else:
                    diff_sum+=int(num[i])
            else:
                if num[i]=="?":
                    diff_count-=1
                else:
                    diff_sum-=int(num[i])


        if diff_count%2!=0:
            return True
        if diff_sum +diff_count//2 *9 ==0:
            return False
        return True                                   
        