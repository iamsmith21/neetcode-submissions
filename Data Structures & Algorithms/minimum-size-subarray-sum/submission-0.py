class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        bestLen = 100001

        sum = 0

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                bestLen = min(bestLen, right - left + 1)

                sum = sum - nums[left]
                left += 1
        
        if bestLen == 100001:
            return 0
        return bestLen