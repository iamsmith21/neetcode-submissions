class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        if len(nums) <= 1:
            return True
        
        dict1 = {}

        for i in range(1, len(nums)):
            dict1[nums[i - 1]] = nums[i]

        res = []
        for k,v in dict1.items():
            if (k % 2 == 0) and ( v % 2 != 0):
                res.append(True)
            elif ( k % 2 != 0 and v % 2 == 0):
                res.append(True)
            else:
                res.append(False)

        if False in res:
            return False
        else:
            return True