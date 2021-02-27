class Solution:
    def totalMoney(self, n: int) -> int:
        sum=0
        b=n%7
        a=n//7
        sum=sum+(((a)*(2*28+(a-1)*7))/2)
        if(b!=0):
            sum=sum+((b*(2*(a+1)+(b-1)))/2)
        return int(sum)
