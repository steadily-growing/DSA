class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adj_list = defaultdict(list)

        for i , j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        
        visited = set()
        def dfs(node):

            if node == destination:
                return True

            if node not in visited:
                visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited and dfs(neighbor):
                    return True
            return False
        
        return dfs(source)

            