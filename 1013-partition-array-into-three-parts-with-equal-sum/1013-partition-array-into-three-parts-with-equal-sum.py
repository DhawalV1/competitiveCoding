class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        
        total = sum(A)
        if total % 3 != 0: return False
        count, cumsum, target = 0, 0, total // 3
        for num in A:
            cumsum += num
            if cumsum == target:
                cumsum = 0
                count += 1
        return count >= 3
        