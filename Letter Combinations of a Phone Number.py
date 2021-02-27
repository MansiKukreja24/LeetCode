class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        if(len(digits)==0):
            return []
        res=[]
        self.solve(digits,dict,res)
        return res
    def solve(self,digits,dict,res,current_string="",current_level=0):
        if current_level==len(digits):
            res.append(current_string)
            return
        for i in dict[int(digits[current_level])]:
            self.solve(digits,dict,res,current_string+i,current_level+1)
