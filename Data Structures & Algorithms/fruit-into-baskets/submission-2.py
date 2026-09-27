class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        freq = {}
        best = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            freq[fruit] = freq.get(fruit, 0) + 1

            while len(freq) > 2:
                freq[fruits[left]] -= 1

                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                
                left += 1
            
            best = max(best, right - left + 1)
        
        return best