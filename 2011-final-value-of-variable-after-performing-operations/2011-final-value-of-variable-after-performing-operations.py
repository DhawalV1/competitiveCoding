class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        l = 0
        for i in operations:
            if i[1] == '-':
                l -= 1
            else:
                l += 1
                
        return l