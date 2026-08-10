# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):

        lenA=0
        lenB=0
        curr=headA
        curr1=headB
        while curr:
            curr=curr.next
            lenA+=1
        while curr1:
            curr1=curr1.next
            lenB+=1    
        diff=abs(lenA-lenB)
        curr=headA
        curr1=headB
        
        if lenA>lenB:
            while diff!=0:
                curr=curr.next
                diff-=1
        else:
            while diff!=0:
                curr1=curr1.next
                diff-=1

        while curr and curr1:
            if curr==curr1:
                return curr

            curr=curr.next
            curr1=curr1.next
           
        return None                        
        