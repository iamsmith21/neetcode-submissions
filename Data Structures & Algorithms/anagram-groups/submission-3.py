class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        resList = []
        
        for i in strs:
            sortedElement = "".join(sorted(i))
            if sortedElement not in hmap:
                hmap[sortedElement] = []
            hmap[sortedElement].append(i)

        for values in hmap.values():
            resList.append(values)
            
        return resList