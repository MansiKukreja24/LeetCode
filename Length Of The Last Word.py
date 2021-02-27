class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word=s.split()
        if(len(word)==0):
            return 0
        else:
            return len(word[-1])
        
