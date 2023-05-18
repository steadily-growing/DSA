# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        
        1->2->2->1
                    f
             s
        1->2->2<-1<-None
        l        r
            l r
              s      prev
        1->2->2->1->None
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
                nxt = slow.next
                slow.next = prev
                prev = slow
                slow = nxt

        
        left, right = head , prev
        while right:
            if left.val != right.val:
                    return False
            left = left.next
            right = right.next
        return True

