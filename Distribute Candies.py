class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        m=n//2
        s=set(candyType)
        k=len(s)
        if(k>=m):
            return m
        return k
