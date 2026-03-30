"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = curr.next.next

        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None 
            curr = curr.next.next
        

        dummy = dummy_curr = Node(0)
        
        curr = head

        while curr:
            dummy_curr.next = curr.next
            curr.next = curr.next.next
            curr = curr.next
            dummy_curr = dummy_curr.next
        return dummy.next







