class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head ==None:
            return None
        p1 = head
        p2 = head.next
        odd = p2
        while p1.next and p2.next:
            p1.next = p2.next
            p2.next = p1.next.next
            p1 = p1.next
            p2 =p2.next
        p1.next = odd
        return head