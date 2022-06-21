# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = None
        if not head:
            return
        while head is not None:
            if head.val == val:
                    head=head.next
            else:
                result = head
                break
                    
        
        while head:
            if head.next and head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return result
        