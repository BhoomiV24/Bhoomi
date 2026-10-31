class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        memo = {}
        
        def get_jump(r: int, c: int, d: int) -> tuple[int, int]:
           
            if r >= m or c >= n:
                return (r, c)
            if grid[r][c] == 0:
                return (r, c)
            
            state = (r, c, d)
            if state in memo:
                return memo[state]
            
           
            if d == 0:
                next_r, next_c, next_d = r + 1, c, 1
            else:
                next_r, next_c, next_d = r, c + 1, 0
                
            res = get_jump(next_r, next_c, next_d)
            memo[state] = res
            return res

       
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for r in range(m):
            for c in range(n):
                if dp[r][c] == 0:
                    continue
                
                
                nr, nc = get_jump(r, c + 1, 0)
                if nr < m and nc < n:
                    dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD
                
                
                nr, nc = get_jump(r + 1, c, 1)
                if nr < m and nc < n:
                    dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD
        
        return dp[m - 1][n - 1]        