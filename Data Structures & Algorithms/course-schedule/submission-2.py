class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prerequisitesMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prerequisitesMap[crs].append(pre)

        visitSet = set()

        def dfs(course):
            if course in visitSet:
                return False

            if prerequisitesMap[course] == []:
                return True

            visitSet.add(course)
            for i in prerequisitesMap[course]:
                if not dfs(i):
                    return False
            
            visitSet.remove(course)
            prerequisitesMap[course] = []

            return True
    
        for course in range(numCourses):
            if not dfs(course): return False
        return True

            

                    



