class Solution:
    def hammingWeight(self, n: int) -> int:
     # 1 = 2^0 2 = 2^1 3
        count = 0

        while n:
            if (n & 1 == 1):
                count += 1
            n = n >> 1
            
        return count