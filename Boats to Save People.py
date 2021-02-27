class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        boat=0
        people.sort()
        i=0
        j=n-1
        res=0
        while(i<=j):
            if(people[i]+people[j]<=limit):
                i=i+1
                j=j-1
            else:
                j=j-1
            res=res+1
        return res
