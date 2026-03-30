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
        
        co = 0
        while curr_a and curr_b:
            curr_dummy.next = ListNode()
            curr_dummy.next.val = (co + curr_a.val + curr_b.val) % 10
            co = (co + curr_a.val + curr_b.val) // 10
            curr_dummy = curr_dummy.next
            curr_a, curr_b = curr_a.next, curr_b.next
        if curr_a or curr_b:
            remain = curr_a if curr_a else curr_b
            while remain:
                curr_dummy.next = ListNode() 
                curr_dummy.next.val = (co + remain.val) % 10
                co = (co + remain.val) // 10
                remain, curr_dummy = remain.next, curr_dummy.next
        if co != 0:
            curr_dummy.next = ListNode()
            curr_dummy.next.val = co
        return dummy.next
