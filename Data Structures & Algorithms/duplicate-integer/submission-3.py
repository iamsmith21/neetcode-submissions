class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        if len(nums) == 0:
            return False

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for value in count.values():
            if value > 1:
                return True

        return False