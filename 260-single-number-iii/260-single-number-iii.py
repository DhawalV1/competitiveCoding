class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        n1 = 0
        n2 = 0
        p=reduce(operator.xor,nums)
        bit = p & ~(p-1)
        for num in nums:
            if num&bit>0:
                n1^=num
            else:
                n2^=num
                
        return [n1,n2]