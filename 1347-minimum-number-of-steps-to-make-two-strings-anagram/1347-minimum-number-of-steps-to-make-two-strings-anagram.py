from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        dict1 = Counter(s)
        dict2 = Counter(t)
        print(dict1,dict2)
        for key in dict2.keys():
            if key in dict1:
                if (dict2[key]-dict1[key])>0:
                    res += dict2[key]-dict1[key]
                print(7)
            else:
                res += dict2[key]
                
        return res