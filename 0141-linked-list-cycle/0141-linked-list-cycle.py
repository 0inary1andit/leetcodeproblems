# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        visited={}
        curr=head
        while curr:
            if curr not in visited:
                visited[curr]=1
                curr=curr.next
            else:
                return True 

        
        return False
       
        