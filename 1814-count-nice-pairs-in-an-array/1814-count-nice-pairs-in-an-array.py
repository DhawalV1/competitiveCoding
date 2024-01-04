class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10**9+7
        modi = []
        mapi = {}
        
        for l in nums:
            if l == 0:
                modi.append(0)
            else:
                
                modi.append(l - int(str(l)[::-1].strip('0')))
        #print(modi)
        
        for i in modi:
            if i in mapi:
                mapi[i] += 1
            else:
                mapi[i] = 1
        sumi = 0
        for key in mapi.keys():
            sumi += ((mapi[key]-1)*mapi[key]//2)%mod
        return sumi%mod
            
        
        
        
            
            
        
        