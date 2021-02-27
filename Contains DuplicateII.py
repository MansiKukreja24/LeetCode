class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s={}
        n =len(nums)
        for i in range(n):
            if nums[i] in s and k >= i-s[nums[i]]:
                    return True
            else:
                s[nums[i]]=i
                
        
        return False
