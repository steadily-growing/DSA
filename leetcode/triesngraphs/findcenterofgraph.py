class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        visited = set()

        for edge in edges:
            for vertex in edge:
                if vertex in visited:
                    return vertex
                else:
                    visited.add(vertex)
        return -1
                
        