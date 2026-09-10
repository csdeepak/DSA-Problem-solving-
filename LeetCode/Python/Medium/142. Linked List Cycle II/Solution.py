# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        a=head
        b=head
        while b is not None and b.next is not None:
            a=a.next
            b=b.next.next
            if a == b:
                break 
        else:
            return None
        a=head
        while a!=b:
            a=a.next
            b=b.next
            
        return a



        