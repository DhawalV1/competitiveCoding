class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = [] 
        while head: 
            nodes.append(head) # push each node in list
            head = head.next # keep moving
        return nodes[(len(nodes))//2]
        