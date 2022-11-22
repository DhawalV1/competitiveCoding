class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        for i in range(len(s)//2):
            s[i],s[len(s)-1-i] = s[len(s)-1-i],s[i]
        
        
        
        """
        if len(s)==1 or len(s)==0:
            return s
        return [s[-1]] + self.reverseString(s[0:len(s)-1])
        """
        """
        Do not return anything, modify s in-place instead
        
        """
    