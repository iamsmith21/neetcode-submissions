class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0 
        c = 0

        for i in nums:
            if i == 1:
                c += 1
                m = max(c, m)
            else:
                c = 0
        return m