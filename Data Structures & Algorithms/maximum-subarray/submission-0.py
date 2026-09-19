class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        best = nums[0]

        for i in range(1,len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            best = max(best, currentSum)

        return best