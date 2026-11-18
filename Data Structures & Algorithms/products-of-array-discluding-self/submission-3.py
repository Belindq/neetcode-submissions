class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #naive approach is to loop through each index and loop through too get prod
        # have prefix and post fix array
        sums=[1]*len(nums)
        prefix=[1]*len(nums)
        postfix=[1]*len(nums)
        for n in range(1,len(nums)):
            prefix[n]=prefix[n-1] *nums[n-1]
       
        for m in range(len(nums)-2, -1, -1): 
            postfix[m]=postfix[m+1] * nums[m+1]
        
        for each in range(len(nums)):
            sums[each]=prefix[each]*postfix[each]
        return sums