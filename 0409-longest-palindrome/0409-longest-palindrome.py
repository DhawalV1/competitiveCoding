class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        maxi = 0
        mapi = {}
        for i in s:
            if i in mapi:
                mapi[i] += 1
            else:
                mapi[i] = 1
                
        for key in mapi.keys():
            if mapi[key]%2:
                count += mapi[key] - 1
                maxi = max(maxi,mapi[key])
            else:
                count += mapi[key]
        if maxi == 0:
            return count
        else:
            return count + 1