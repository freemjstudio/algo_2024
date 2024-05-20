class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+3)
        
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        if n <= 3:
            return dp[n]
        
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]