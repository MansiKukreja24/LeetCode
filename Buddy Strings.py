class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if(len(A)!=len(B)):
            return False
        elif (sorted(A)!=sorted(B)):
            return False
        elif A==B and len(set(A))==len(A):
            return False
        else:
            c=0
            for i in range(len(A)):
                if(A[i]!=B[i]):
                    c+=1
                    if c==3:
                        return False
            return True
        
       
