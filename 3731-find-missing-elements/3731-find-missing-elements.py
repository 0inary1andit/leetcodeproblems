class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        data = list(range(min(nums), max(nums)+1))
        result=[]

        for i in data:
            if i not in nums:
                result.append(i)


        return result    


        

 
        