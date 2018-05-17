class Solution:
	def removeElements(self,head,val):
		new = ListNode(0)
		new.next = head
		cur = new
		while cur.next:
			if cur.next.val == val:
				delNode = cur.next
				cur.next = delNode.next
			else:
				cur = cur.next
		return new.next