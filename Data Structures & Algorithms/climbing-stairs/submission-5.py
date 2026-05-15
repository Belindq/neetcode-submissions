class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}

        def ways(k) -> int:
            if k==1:
                return 1
            elif k==2:
                return 2
            
            if k in memo:
                return memo[k]
            
            memo[k]=ways(k-1)+ways(k-2)
            return memo[k]
        return ways(n)
            

