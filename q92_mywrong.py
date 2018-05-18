class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        while m==n:
            return head
        
        lenth = 1
        cal_p =head
        while cal_p != None:
            cal_p = cal_p.next
            lenth += 1
        cur = head 
        pres = None
        while m==1 and n == lenth-1:
            cur == head
            pres == None
            while cur != None:
                next_ = cur.next
                cur.next = pres
                pres = cur
                cur = next
            return pres
                  
        temp = head
        m_point = None
        pre_m = None
        n_point = None
        next_n = None
        for i in range(n):
            if i == m-2:
                pre_m = temp
                m_point = temp.next
            if i == n-1:
                n_point = temp
                next_n = temp.next
            temp = temp.next
        
        cur = m_point
        pre = next_n
        while cur != next_n:
            next_ = cur.next
            cur.next = pre
            pre = cur 
            cur = next_
        pre_m.next = pre
        return head
            
                