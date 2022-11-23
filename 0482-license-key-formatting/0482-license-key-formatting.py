class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = ''
        count = 0  
        s.strip("-")
        for j in range(len(s)-1,-1,-1):
            if s[j]!='-':
                if 97<=ord(s[j]) and ord(s[j])<=123:
                    res = chr(ord(s[j])-32) + res
                else:
                    res = s[j] + res
                count += 1
            if count == k:
                res = '-' + res
                count = 0
        return res[1::] if count==0 else res