class Solution:
    def countAndSay(self, n: int) -> str:
        if(n==1):
            return "1"
        if(n==2):
            return "11"
        s="11"
        for i in range(3,n+1):
            s+='k'
            l=len(s)
            c=1
            tmp=''
            for j in range(1,l):
                if(s[j]!=s[j-1]):
                    tmp+=str(c+0)
                    tmp+=s[j-1]
                    c=1
                else:
                    c+=1
            s=tmp
        return s
        
