class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        initialCount = 0
        for i in flowerbed:
            if i == 1:
                initialCount += 1

        count = initialCount

        for i in range(len(flowerbed)):
            leftEmpty = (i == 0 or flowerbed[i - 1] == 0)
            rightEmpty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            
            if flowerbed[i] == 0 and leftEmpty and rightEmpty:
                flowerbed[i] = 1
                count += 1  

        return count >= (initialCount + n)