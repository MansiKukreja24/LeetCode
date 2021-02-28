class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words=sentence.split(" ")
        m=len(sentence)
        n=len(searchWord)
        
        for i in range(len(words)):
            s=words[i]
            if(len(s)>=n):
                if(s[:n]==searchWord):
                    return i+1
                
        return -1
