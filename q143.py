class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head ==None or head.next== None:
            return
        p1 = head
        p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        
        pmiddle = p1
        cur = pmiddle.next
        pre = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        pmiddle.next = pre
        
        p1 = head
        p2 = pmiddle.next
        while p1 != pmiddle:
            pmiddle.next =p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = pmiddle.next
            