from itertools import permutations
class Solution:
    def maxCompatibilitySum(self,s: List[List[int]], mentors: List[List[int]]) -> int:
        side = len(s)
        mat = [[0]*len(s) for _ in range(len(s))]
        n = len(s[0])
        for i in range(len(s)):
            
            for j in range(len(s)):
                sumi = 0
                for k in range(n):
                    if s[j][k] == mentors[i][k]:
                        sumi += 1
                        
                mat[i][j] = sumi
               
        return self.MaxSum(side,mat)
                
    def MaxSum(self,side, matrix):
         
        s = ''
        # Generating the string
        for i in range(0, side):
            s = s + str(i)

        # Permutations of s string
        permlist = permutations(s)

        # List all possible case
        cases = []

        # Append all possible case in cases list
        for perm in list(permlist):
            cases.append(''.join(perm))

        # List to store all Sums
        sum = []

        # Iterate over all case
        for c in cases:
            p = []
            tot = 0
            for i in range(0, side):
                p.append(matrix[int(s[i])][int(c[i])])
        
            for i in range(side-1, -1, -1):
                tot = tot + p[i]
            sum.append(tot)


        # Maximum of sum list is
        # the max sum
        return max(sum)


        #ans = 0 
        #for perm in permutations(range(m)): 
         #   ans = max(ans, sum(score[i][j] for i, j in zip(perm, range(m))))
        #return ans 
        
        
        
      