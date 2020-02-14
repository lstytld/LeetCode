# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        flag = 0
        ans = ListNode(0)
        cur = ans
        while (l1 and l2) or flag == 1:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            l = l1_val + l2_val + flag
            cur.next = ListNode(l % 10)
            cur = cur.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            flag = l // 10

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return ans.next


