# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        sumi = 0
        while head:
            sumi = sumi + head.val * 2**(count-1)
            count -= 1
            head = head.next
        return sumi
            
        