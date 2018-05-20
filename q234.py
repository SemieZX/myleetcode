class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next == None:
            return Tru
        slow = fast = head
        pre = None

        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next
        pre.next = None

        rev = None
        while slow:
            nxt =slow.next
            slow.next = rev
            rev = slow
            slow = nxt
        while rev and head:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        return True