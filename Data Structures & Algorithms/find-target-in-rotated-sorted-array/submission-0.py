class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(self, nums: List[int], left: int, right: int, target: int) -> int:
            middle = int(left + (right-left)/2)
            if left> right:
                return -1
            elif nums[middle] ==target:
                return middle
            elif nums[left]<=nums[middle]:
                if nums[middle]>=target>=nums[left]:
                    return search(self, nums, left, middle-1, target)
                else:
                    return search(self, nums, middle+1, right, target)
            elif nums[right]>=nums[middle]:
                if nums[middle]<=target<=nums[right]:
                    return search(self, nums, middle+1, right, target)
                else:    
                    return search(self, nums, left, middle-1, target)

        return search(self, nums, 0, len(nums)-1, target)

            

