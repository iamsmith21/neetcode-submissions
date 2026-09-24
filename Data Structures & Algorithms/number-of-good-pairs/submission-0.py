class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        

        count = 0
        for l in range(len(nums)):
            r = l + 1
            while r < len(nums):
                if nums[l] == nums[r]:
                    count += 1
                r += 1

        return count
            