# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr_dummy = ListNode()
        curr_a = l1
        curr_b = l2
        carry = 0
        while curr_a or curr_b or carry:
            a = curr_a.val if curr_a else 0
            b = curr_b.val if curr_b else 0

            carry, val = divmod(a+b+carry, 10)
            curr_dummy.next = ListNode(val)

            curr_dummy = curr_dummy.next
            if curr_a: curr_a = curr_a.next 
            if curr_b: curr_b = curr_b.next 
        return dummy.next