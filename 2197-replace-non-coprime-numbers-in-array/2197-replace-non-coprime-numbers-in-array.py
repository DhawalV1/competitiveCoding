class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        
        st = [nums[0]]
        
        for n in nums[1:]:
            
            st.append(n)
            
            while len(st)>=2 and math.gcd(st[-1],st[-2])>1:
                
                a = st.pop()
                b = st.pop()
                st.append(a*b//math.gcd(a,b))
                
        return st