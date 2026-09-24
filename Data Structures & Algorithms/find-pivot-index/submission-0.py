class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        def findSum(left, right):
            subSum = 0
            for i in range(left, right):
                subSum += nums[i]
            
            return subSum
        
        for i in range(len(nums)):
            lSum = findSum(0, i)
            rSum = findSum(i+1, len(nums))

            if lSum == rSum:
                return i
        
        return -1