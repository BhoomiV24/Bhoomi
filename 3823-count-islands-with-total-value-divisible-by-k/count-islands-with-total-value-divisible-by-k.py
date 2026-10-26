class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if (r < 0 or r >= m or c < 0 or c >= n
                    or grid[r][c] == 0):
                return 0

            # Mark the cell as visited
            value = grid[r][c]
            grid[r][c] = 0

            # Explore all four directions
            value += dfs(r + 1, c)
            value += dfs(r - 1, c)
            value += dfs(r, c + 1)
            value += dfs(r, c - 1)

            return value

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    total = dfs(i, j)

                    if total % k == 0:
                        count += 1

        return count        