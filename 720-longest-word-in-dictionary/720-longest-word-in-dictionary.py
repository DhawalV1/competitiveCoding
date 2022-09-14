
class Solution:
    def longestWord(self, words: List[str]) -> str:
        valid = set([""])
       
        for word in sorted(words, key=lambda x: len(x)):
           print(word[:-1])
           if word[:-1] in valid:
                valid.add(word)
                
        print(valid)
								
        return max(sorted(valid), key=lambda x: len(x))