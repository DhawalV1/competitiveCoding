class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        num1 = edges[0][0]
        num2 = edges[0][1]
        if num1 in edges[1]:
            return num1
        else:
            return num2