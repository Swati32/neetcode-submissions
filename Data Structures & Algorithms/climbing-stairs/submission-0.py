class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        cache[0] = 1
        cache[1] = 1

        def dfs(n):
            if n in cache:
                return cache[n]
            cache[n] = dfs(n-1) + dfs(n-2)
            return cache[n]
            
        return dfs(n)
        