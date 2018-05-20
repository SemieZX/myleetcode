class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dymmyHead = ListNode(0)
        pre = dymmyHead
        cur = head
        while cur:
            nxt = cur.next
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = dymmyHead
            cur = nxt
        return dymmyHead.next