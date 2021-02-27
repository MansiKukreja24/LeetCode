class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if(n==1):
            return 0
        i=0
        buy_amt=0
        sell_amt=0
        while(i<(n-1)):
            while((i<(n-1)) and (prices[i+1])<=prices[i]):
                i+=1
            if(i==n-1):
                break
            buy=i
            i+=1
            while((i<n) and (prices[i])>prices[i-1]):
                i+=1
            sell=i-1
            buy_amt+=prices[buy]
            sell_amt+=prices[sell]
        return (sell_amt-buy_amt)
