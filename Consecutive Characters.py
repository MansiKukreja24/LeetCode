class Solution:
    def maxPower(self, s: str) -> int:
        res=1
        c=1
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                c+=1
            else:
                c=1
            res=max(res,c)
        return res
