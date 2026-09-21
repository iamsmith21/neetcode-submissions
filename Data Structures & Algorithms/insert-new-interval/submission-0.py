class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []

        newStart = newInterval[0]
        newEnd = newInterval[1]

        for i in range(len(intervals)):
            # BEFORE
            start = intervals[i][0]
            end = intervals[i][1]
            if end < newStart:
                result.append([start,end])
            # AFTER
            elif start > newEnd:
                return result + [[newStart,newEnd]] + intervals[i:]
            else:
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)
        result.append([newStart, newEnd])
        

        return result
