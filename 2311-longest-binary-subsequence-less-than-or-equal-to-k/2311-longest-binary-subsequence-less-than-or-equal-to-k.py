class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        sumi = 0
        pow_two=0

        cnt=0
        for i in s[::-1]:
            if i=='0': # you can take any number of zeros you want it never contribute to the sum 
                cnt+=1

            else:
                if sumi+2**pow_two<=k: # until it is less than k.otherwise we can skip if it exceeds k.
                    sumi+=2**pow_two
                    cnt+=1


            pow_two+=1


        return cnt