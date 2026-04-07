class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            
            
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 0 or (r, c) in visit:
                return 0
            visit.add((r, c))
            area = 0
            area = 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
            return area
        area = 0
        for r in range(rows):
            for c in range(cols):
                a = dfs(r, c)
                area = max(area, a)
        return area