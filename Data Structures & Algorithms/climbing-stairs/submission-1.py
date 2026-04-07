class Solution:
    def climbStairs(self, n: int) -> int:

        i = 0
        cache = {}
        def dp(i):
            if i == n - 1:
                return 1
            if i == n - 2:
                return 2
            if i in cache:
                return cache[i]

            cache[i] = dp(i+1) + dp(i+2)
            return cache[i]
        return dp(0)

        