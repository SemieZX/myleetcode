class Solution():
	def reverseList(self,head):
		pre = None
		cur = head
		while cur != None:
			next = cur.next
			cur.next= pre
			pre = cur
			cur = next
		return pre