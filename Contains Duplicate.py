class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set(nums)
        n=len(nums)
        m=len(s)
        if((n-m)>0):
            return True
        else:
            return False
