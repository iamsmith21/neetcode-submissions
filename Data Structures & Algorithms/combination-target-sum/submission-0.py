class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, sol = [], []
        total = 0

        def backtracking(i, total):
            if total==target:
                result.append(sol[:])
                return
            
            if total > target:
                return
            
            for j in range(i,len(nums)):
                sol.append(nums[j])
                backtracking(j, total+nums[j])
                sol.pop()


        backtracking(0, 0) 
        return result