class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        
        for i in range(len(prices)): 
            largest = max(prices[i:len(prices)])
            if largest-prices[i]>m:
                m =largest-prices[i]

        return m
            
