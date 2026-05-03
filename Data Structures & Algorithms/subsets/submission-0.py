class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        tempSol = []
        n = len(nums)

        def backtracking(i):
            if i==n:
                result.append(tempSol[:])
                return 
        
            #First Branch
            backtracking(i+1)

            #Second Branch with number in the array
            tempSol.append(nums[i])
            backtracking(i+1)
            tempSol.pop()
        
        backtracking(0)
        return result
