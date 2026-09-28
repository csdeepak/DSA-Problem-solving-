# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy=ListNode(0)
        dummy.next=head
        leftprev,cur=dummy,head
        for i in range(left-1):
            leftprev,cur=cur,cur.next
        
        prev=None
        for _  in range(right-left+1):
            after=cur.next
            cur.next=prev
            prev=cur
            cur=after
        leftprev.next.next=cur
        leftprev.next=prev
            
        
        return head
        