class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxRate = max(piles)
        minRate=1
        ranges=range(minRate, maxRate)
        rate = (maxRate+minRate)//2
        hh=0
        while maxRate>minRate:
            hh=0
            rate = (maxRate+minRate)//2
            for banana in piles:
                hh+=math.ceil(banana/rate)
            if hh<=h:
                maxRate=rate
            elif hh>h:
                minRate=rate+1
            
        return minRate


                

        