class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binsearch(self, nums: List[int], left: int, right:int, target: int) -> int:
            middle =int(left+ (right-left)/2)
            if left>right:
                return -1
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                return binsearch(self, nums, left, middle-1, target)
            else:
                return binsearch(self, nums, middle+1, right, target)
        return binsearch(self, nums, 0, len(nums)-1, target)
        