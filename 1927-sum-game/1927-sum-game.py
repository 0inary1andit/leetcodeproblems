class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n=len(num)
        sum_left=0
        sum_right=0
        count_left=0
        count_right=0

        for i in range(n):
            if i<n//2:
                if num[i]=="?":
                    count_left+=1
                else:
                    sum_left+=int(num[i])
            else:
                if num[i]=="?":
                    count_right+=1
                else:
                    sum_right+=int(num[i])
        
        if (count_left+count_right)%2!=0:
            return True

        if (sum_left-sum_right)+(count_left-count_right)//2 *9==0:
            return False

        return True

