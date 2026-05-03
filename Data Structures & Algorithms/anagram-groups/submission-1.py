class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalDict = defaultdict(list)
        for word in strs:
            count = [0] *26
            for c in word:
                count[ord(c)-ord('a')] +=1
            finalDict[tuple(count)].append(word)
        return list(finalDict.values())