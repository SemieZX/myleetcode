class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        fakeNode = ListNode(0)
        fakeNode.next = head
        pre = fakeNode
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next ==cur:
                pre = pre.next
            else:
                pre.next  = cur.next
            cur = cur.next
        return fakeNode.next