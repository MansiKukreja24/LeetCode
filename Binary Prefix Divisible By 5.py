class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        st=""
        res=[]
        for i in range(len(A)):
            st=st+str(A[i])
            if(int(st,2)%5==0):
                res.append(True)
            else:
                res.append(False)
               
        return res
                
        
