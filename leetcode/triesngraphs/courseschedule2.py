class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for crs, preq in prerequisites:
            graph[crs].append(preq)
        
        output =[]
        visited , cycle = set(), set()
        def complete(crs):
            if crs in visited:
                return True
            
            if crs in cycle:
                return False

            cycle.add(crs)
            for preq in graph[crs]:
                if not complete(preq):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not complete(c):
                return []
        return output
            

            
