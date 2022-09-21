class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        evenSum = 0
        answer = []
        numsCopy = nums[:]
        
        for num in numsCopy:
            if num % 2 == 0:
                evenSum += num
        
        for val, index in queries:
            oldVal = numsCopy[index]
            if oldVal % 2 == 0:
                evenSum -= oldVal
            
            newVal = numsCopy[index] + val
            numsCopy[index] = newVal
            
            if newVal % 2 == 0:
                evenSum += newVal
            answer.append(evenSum)
            
        return answer