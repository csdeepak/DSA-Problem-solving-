class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head

        leftprev, cur = dummy, head

        # Move cur to the left position
        for i in range(left - 1):
            leftprev, cur = cur, cur.next

        # Reverse from left to right
        prev = None

        for _ in range(right - left + 1):
            after = cur.next
            cur.next = prev
            prev = cur
            cur = after

        # Connect the reversed portion
        leftprev.next.next = cur
        leftprev.next = prev

        return dummy.next