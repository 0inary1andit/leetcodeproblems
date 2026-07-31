class Solution(object):
    def findLHS(self, nums):
        count={}
        lenght=0

        for i in range(len(nums)):
            if (nums[i] not in count):
                count[nums[i]]=1
            else:
                count[nums[i]]=count[nums[i]]+1

        for key in count:
            if key+1 in count:
                lenght=max(lenght,count[key]+count[key+1])


        return lenght       

        