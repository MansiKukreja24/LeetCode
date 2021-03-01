class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr=1
        prev=0
        c=0
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                curr+=1
            else:
                prev=curr
                curr=1
            if(prev>=curr):
                c+=1
                
        return c
