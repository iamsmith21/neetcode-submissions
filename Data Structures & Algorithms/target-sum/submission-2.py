class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def findSum(index, curr_sum):

            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]

            if index >= len(nums):
                if curr_sum == target:
                    return 1
                return 0

            ways = (findSum(index + 1, curr_sum + nums[index]) + findSum(index + 1, curr_sum - nums[index]))
            memo[(index, curr_sum)] = ways
            return memo[(index, curr_sum)]

        curr_sum = 0
        memo = {}

        return findSum(0,curr_sum)