class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[[]]
        for i in s:
            if i.isalpha():
                for j in range(len(res)):
                    res.append(res[j][:])
                    res[j].append(i.lower())
                    res[-1].append(i.upper())
            else:
                for k in res:
                    k.append(i)
        return map("".join,res)
    
       
        
