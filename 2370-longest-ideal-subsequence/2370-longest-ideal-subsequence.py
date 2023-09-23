class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0]*26

        for ch in s:
            index = ord(ch)-ord("a")
            dp[index] = max(dp[max(index-k,0):min(index+k+1,26)]) + 1

        return max(dp)