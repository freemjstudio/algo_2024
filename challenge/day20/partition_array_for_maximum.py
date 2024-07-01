# https://leetcode.com/problems/partition-array-for-maximum-sum/description/

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n+1)
        
        for i in range(1, n+1):
            max_val = -int(1e9) # max 값을 찾아야 함 
            
            
            # sub array 길이 
            for j in range(1, min(k, i)+1):
                max_val = max(max_val, arr[i-j])
                
                dp[i] = max(dp[i], dp[i - j] + max_val * j)
                
            
        
        return dp[n]