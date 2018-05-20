class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        p = q = dummyHead
        for i in range(n+1):
            q = q.next
        while q :
            p = p.next
            q = q.next
        p.next  = p.next.next
        return dummyHead.next