class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        if len(nums) <= 1:
            return True
        
        l ,r = 0, 1

        while r < len(nums):
            if nums[l]%2 == 0 and nums[r] % 2 == 0:
                return False
            if nums[l]%2 == 1 and nums[r]% 2 ==1:
                return False

            l += 1
            r += 1
        
        return True