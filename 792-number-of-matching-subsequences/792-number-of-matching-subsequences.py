from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_dict = defaultdict(list)
        count = 0
        for word in words:
            word_dict[word[0]].append(word)  
        for c in s:
            words_expecting_char = word_dict[c]
            word_dict[c] = []
            for word in words_expecting_char:
                if len(word)==1:
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        return count
        
       