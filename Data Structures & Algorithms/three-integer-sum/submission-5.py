class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        x=0
        y=len(nums)-1
        ans=set()
        for i in range(len(nums)):
            x=i+1
            y=len(nums)-1
            while x<y:
                if nums[x]+nums[y]==-nums[i]:
                    if (nums[i],nums[x],nums[y]) not in ans:
                        
                        ans.add((nums[i],nums[x],nums[y]))
                    x+=1
                    y-=1
                elif nums[x]+nums[y] < -nums[i]:
                    x+=1                 
                else:
                    y-=1
                    
        return list(ans)
            