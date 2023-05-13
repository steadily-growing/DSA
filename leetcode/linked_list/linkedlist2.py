# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
       slow, fast = head, head

       while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
           if slow == fast: break

       else:
            return None

      

       p1 =  head
       p2 =  slow

       while p1!=p2:
            p1 = p1.next
            p2 = p2.next
        
       return p2


    
        
            