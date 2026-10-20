class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lowest=0
        minrate= 1
        maxrate = max(piles)
        while minrate<maxrate:
            midrate =(minrate+maxrate)//2;
            midh =self.checkmid(piles,midrate,h) 
            if  midh<=h:
                maxrate=midrate
            elif midh>h:
                minrate=midrate+1
        return minrate

        
    def checkmid (self, piles: List[int], rate:int, hh:int)->int:
        h =0
        for pile in piles:
            h+=math.ceil(pile/rate)
        return h



