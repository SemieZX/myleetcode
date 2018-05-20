class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        lenth = 1
        newH = tail = head
        while tail.next:
            tail = tail.next
            lenth += 1
        tail.next = head #cirle the link
        k %= lenth
        if k != 0:
            for i in range(lenth-k):
                tail = tail.next
        newH = tail.next
        tail.next = None
        return newH


#slow and fast pointers
class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or head.next ==None:
            return head
        dummyh = ListNode(0)
        dummyh.next =head
        fast = slow = dummyh
        lenth = 0
        while fast.next:
            fast = fast.next
            lenth += 1
        for i in range(lenth -k%lenth ):
            slow = slow.next
        fast.next = dummyh.next
        dummyh.next = slow.next
        slow.next = None
        return dummyh.next
