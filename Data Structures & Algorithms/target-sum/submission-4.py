class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def solve(index, curr_sum):

            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]

            if index == len(nums):
                if curr_sum == target:
                    return 1
                return 0

            plus = solve(index + 1, curr_sum + nums[index])
            minus = solve(index + 1, curr_sum - nums[index])

            ways = plus + minus
            memo[(index, curr_sum)] = ways

            return ways


        
        curr_sum = 0
        memo = {}
        return solve(0,curr_sum)