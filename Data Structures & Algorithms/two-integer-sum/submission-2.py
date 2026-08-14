class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i not in res and j not in res and i != j:
                    res.append(i)
                    res.append(j)
                    break
        
        return res
        