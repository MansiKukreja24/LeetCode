class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s=set(allowed)
        c=0
        for i in range(len(words)):
            res=True
            for j in range(len(words[i])):
                if(words[i][j] not in s):
                    res=False
                    break;
            if(res):
                c+=1
        return c
