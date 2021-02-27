import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        minimum =sys.maxsize - 1
        maximum=0
        for i in range(n):
            if(prices[i]<minimum):
                minimum=prices[i]
            elif(prices[i]-minimum > maximum):
                maximum=prices[i]-minimum
        return maximum
