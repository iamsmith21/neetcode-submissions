class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max = len(nums)/2

        dict1 = {}

        for i in nums:
            dict1[i] = dict1.get(i, 0) + 1
        
        for k,v in dict1.items():
            if v > max:
                return k