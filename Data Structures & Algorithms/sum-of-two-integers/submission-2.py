class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
        
        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        
        return a & mask if (a & mask) <= MAX else ~(a & mask ^ mask)