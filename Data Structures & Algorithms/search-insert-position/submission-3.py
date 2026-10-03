class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            cur = nums[mid]

            if target == cur:
                return mid

            if target < cur:
                right = mid - 1
            
            if target > cur:
                left = mid + 1

        return left


