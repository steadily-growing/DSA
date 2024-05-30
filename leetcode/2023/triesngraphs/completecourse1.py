class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for crs, preq in prerequisites:
            graph[crs].append(preq)
        
        visitedSet = set()
        def complete(crs):
            if crs in visitedSet:
                return False
                
            if graph[crs] == []:
                return True

            visitedSet.add(crs)
            for preq in graph[crs]:
                if not complete(preq):
                    return False
            visitedSet.remove(crs)
            graph[crs] = []
            return True
         
        for c in range(numCourses):
            if not complete(c): return False
        return True
