class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict1 = {}
        # {difference : index}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in dict1:
                return [dict1[diff], i]
            
            dict1[nums[i]] = i

        return []