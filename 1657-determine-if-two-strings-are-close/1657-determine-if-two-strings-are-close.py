class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        col1 = collections.Counter(word1)
        col2 = collections.Counter(word2)
        print(col1,col2)
        arr1 = []
        arr2 = []
        for key in col1.keys():
            if key in col2:
                
                arr1.append(col1[key])
            else:
                return False
        for key in col2.keys():
            if key in col1:
                
                arr2.append(col2[key])
            else:
                return False
        arr1.sort()
        arr2.sort()
        print(arr1,arr2)
        return arr1== arr2