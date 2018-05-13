class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        length = n - m
        new_head = ListNode(0)
        new_head.next = head
        start = new_head
        end = head
        for i in range(m - 1):
            start = start.next
        for i in range(n):
            end = end.next
        for i in range(length):
            temp = start.next
            start.next = temp.next
            if end:
                temp.next = end
            else:
                temp.next = None
            end = temp
        start.next.next = end
        return new_head.next


l1 = ListNode(1)
l1.next = ListNode(2)
l2 = l1.next
l2.next = ListNode(3)
l3 = l2.next
l3.next = ListNode(4)
l4 = l3.next
l4.next = ListNode(5)
Demo = Solution()
result = Demo.reverseBetween(l1,1,5)
while result:
    print(result.val)
    result = result.next