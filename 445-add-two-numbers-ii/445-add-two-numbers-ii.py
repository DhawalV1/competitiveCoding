# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        num1 = 0
        num2 = 0
        while p1:
            num1 = num1*10 + p1.val
            p1 = p1.next
        while p2:
            num2 = num2*10 + p2.val
            p2 = p2.next
        num3 = str(num1 + num2)
        l3 = ListNode(num3[0])
        itr = l3
        for i in range(1,len(num3)):
            itr.next = ListNode(int(num3[i]))
            itr = itr.next
        return l3
        

            
        