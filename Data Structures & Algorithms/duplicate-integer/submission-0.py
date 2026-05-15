class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l2 = []
        for num in nums:
            if num in l2:
                return True
            l2.append(num)

        return False