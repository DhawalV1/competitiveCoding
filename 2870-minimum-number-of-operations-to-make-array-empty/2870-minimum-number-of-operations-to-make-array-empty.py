class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mapi={}
        sumi = 0
        for i in nums:
            if i in mapi:
                mapi[i] += 1
            else:
                mapi[i] = 1
        print(mapi)
        for key in mapi.keys():
            
            if mapi[key]%3==2:
                sumi += (mapi[key]-2)//3 + 1
            elif mapi[key]%3 == 1:
                if mapi[key]==1: return -1
                else:sumi += (mapi[key]-4)//3 + 2
            else:
                sumi += mapi[key]//3
                
        return sumi
        