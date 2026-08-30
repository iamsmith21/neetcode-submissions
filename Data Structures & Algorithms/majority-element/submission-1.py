class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max = len(nums)/2

        dict1 = {}

        for i in nums:
            dict1[i] = dict1.get(i, 0) + 1
            if dict1[i] > max:
                return i

        return None