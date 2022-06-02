# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        n2 = ""
        
        itr1 = l1
        itr2 = l2
        while itr1 or itr2:
            if itr1:
                n1 += str(itr1.val)
                itr1=itr1.next
            if itr2:
                n2+=str(itr2.val)
                itr2=itr2.next
        n1 = n1[::-1]
        n2 = n2[::-1]
        n3 = str(int(n1) + int(n2))[::-1]
        l3 = ListNode(n3[0])
        itr = l3
        for i in range(1,len(n3)):
            itr.next = ListNode(int(n3[i]))
            itr = itr.next
        return l3
        