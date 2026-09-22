class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1 = {} 
        res = []
        # "act" : ["act", cat]
        for s in strs:
            sortedS = "".join(sorted(s))

            if sortedS in dict1: 
                dict1[sortedS].append(s)
            else:
                dict1[sortedS] = []
                dict1[sortedS].append(s)

        for v in dict1.values():
            res.append(v)

        return res

