class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_end = nums[0]
        min_end = nums[0]
        result = nums[0]

        for i in range(1,len(nums)):
            prev_max = max_end
            prev_min = min_end

            max_end = max(nums[i], nums[i]*prev_max, nums[i]*prev_min)
            min_end = min(nums[i], nums[i]*prev_max, nums[i]*prev_min)

            result = max(result, max_end)
        
        return result