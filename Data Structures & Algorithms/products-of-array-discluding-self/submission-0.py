class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums)
        for n in range(len(result)):
            for i in range(len(nums)):
                if i!=n:
                    result[n]*=nums[i]
        return result
                




        