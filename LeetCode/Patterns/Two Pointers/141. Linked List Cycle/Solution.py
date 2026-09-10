class Solution(object):
    def hasCycle(self, head):
        a = head          # slow pointer
        b = head          # fast pointer

        while b is not None and b.next is not None:
            a = a.next
            b = b.next.next

            if a == b:
                return True

        return False