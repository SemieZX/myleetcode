        def reverse(head):
            cur = head
            pre = None
            while cur :
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre
        l1_ = reverse(l1)
        l2_ = reverse(l2)
        root = l3_ = ListNode(0)
        carry = 0
        while l1_ or l2_ or carry:
            v1 = v2 = 0
            if l1_:
                v1 = l1_.val
                l1_ = l1_.next
            if l2_:
                v2 = l2_.val
                l2_ = l2_.next
            carry, value = divmod(v1+v2+carry, 10)
            l3_.next = ListNode(value)
            l3_= l3_.next
        res = reverse(root.next)
        return res
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = [ ]
        s2 = [ ]
        while l1 != None:
            s1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            s2.append(l2.val)
            l2 = l2.next
        sum = 0
        l3 = ListNode(0)
        while s1 or s2:
            if s1:
                sum += s1.pop( )
            if s2:
                sum += s2.pop()
            l3.val = sum%10
            head = ListNode(sum//10)
            head.next = l3
            l3 = head
            sum = sum//10
        if l3.val ==0:
            return l3.next
        else:
            return l3