class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for s in details:
            subStr = s[-4:-2]
            if int(subStr) > 60:
                count += 1

        return count
