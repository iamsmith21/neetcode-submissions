class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        temp = 0
        for i in range(len(height)):
            temp = max(temp, height[i])
            leftMax[i] = temp

        rtemp = 0
        for i in range(len(height) - 1, -1, -1):
            rtemp = max(rtemp, height[i])
            rightMax[i] = rtemp

        res = 0
        for i in range(len(height)):
            res += min(leftMax[i],rightMax[i]) - height[i]
        
        return res