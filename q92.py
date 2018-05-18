class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m == n:
            return head
        root = ListNode(0)
        root.next = head
        prem = pren = root
        while m > 0 or n > 0:
            if m > 0:
                if m == 1:
                    first = prem #point the loop before
                prem = prem.next
                m -= 1
            if n > 0:
                pren = pren.next
                n -= 1
        last = pren.next
        pre = self.helper(prem, pren)
        first.next = pre
        while first.next:
            first = first.next
        first.next = last
        return root.next
    
    def helper(self, prem, pren): #reverse link list
        last = pren; pren.next = None; pre = prem; cur = prem.next; pre.next = None
        while cur and pre != pren:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre