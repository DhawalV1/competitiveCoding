class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        leng = 0
        curr = head
        while curr:
            leng += 1
            curr = curr.next
        mid = leng//2 
        curri = 0
        while head:
            if curri == mid:
                return head
            head = head.next
            curri += 1
        