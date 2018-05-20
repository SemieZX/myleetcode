class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k == 1:
            return head
        num = 0
        dymmyHead = ListNode(0)
        dymmyHead.next = head
        cur =dymmyHead
        pre = dymmyHead
        nxt = dymmyHead
        while cur :
            num += 1
            cur = cur.next
        num -= 1
        while num >= k:
            cur = pre.next
            nxt = cur.next
            for i in range(k-1):
                cur.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt
                nxt = cur.next
            pre = cur
            num -= k
        return dymmyHead.next
        