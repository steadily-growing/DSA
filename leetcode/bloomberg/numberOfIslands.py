class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        res = 0

        def dfs(row, col):
            # Define the directions for DFS: down, right, up, left
            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            # Iterate through all possible directions
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                # Check if the neighbor is within bounds and is a valid island cell
                if 0 <= nr < r and 0 <= nc < c and grid[nr][nc] == '1':
                    # Mark the cell as visited
                    grid[nr][nc] = '0'
                    # Recursive DFS on the neighbor cell
                    dfs(nr, nc)

        # Iterate through the grid to find islands
        for row in range(r):
            for col in range(c):
                # If the cell is part of an unvisited island, perform DFS
                if grid[row][col] == '1':
                    # Mark the cell as visited
                    grid[row][col] = '0'
                    dfs(row, col)
                    res += 1

        return res
