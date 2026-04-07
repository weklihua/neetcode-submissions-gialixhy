class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = {}
        def dfs(r, c):
            if r == m or c == n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if (r, c) in cache:
                return cache[(r, c)]
            

            count = 0
            count = dfs(r + 1, c) + dfs(r, c + 1)
            cache[(r, c)] = count

            return count
        return dfs(0, 0)