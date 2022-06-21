# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        p1 = p2 = head
        
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            
        prev = None
        curr = p1
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  