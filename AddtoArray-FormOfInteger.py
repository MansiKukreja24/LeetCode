class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        s=[str(i) for i in A]
        res=int("".join(s))
        l=[]
        sum=str(res+K)
        for i in sum:
            l.append(i)
        return l
        
