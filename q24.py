class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dymmyHead = ListNode(0)
        dymmyHead.next = head
        
        p  = dymmyHead
        while p.next and p.next.next:
            node1 = p.next
            node2 = node1.next
            next = node2.next
            node2.next = node1
            node1.next = next
            p.next = node2
            p = node1
        return dymmyHead.next