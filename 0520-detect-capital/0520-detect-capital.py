class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        return all('A' <= ch <= 'Z' for ch in word) or all('a' <= ch <= 'z' for ch in word) or ('A' <= word[0] <= 'Z' and all('a' <= ch <= 'z' for ch in word[1:]))
        