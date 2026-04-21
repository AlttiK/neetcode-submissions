class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        resWord = ''
        i = 0
        while i < len(word1) and i < len(word2):
            resWord += word1[i]
            resWord += word2[i]
            i += 1
        
        if i < len(word1):
            resWord += word1[i:]

        if i < len(word2):
            resWord += word2[i:]

        return resWord