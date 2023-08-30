class Solution:

    def minCut(self, s: str) -> int:
        size = len(s)
        dp = [[False] * size for _ in range(size)]  # dp[i][j] will be 'true' if the string from index i to j is a palindrome
        
        for i in range(size):
            dp[i][i] = True
        
        for end in range(size):
            for start in range(end - 1, -1, -1):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
        
        cuts = [0] * size  # cuts[i] represents the minimum cuts needed for the substring s[0:i+1]
        
        for i in range(size):
            min_cuts = i
            for j in range(i + 1):
                if dp[j][i]:
                    min_cuts = 0 if j == 0 else min(min_cuts, cuts[j - 1] + 1)
            cuts[i] = min_cuts
        
        return cuts[size - 1]


    def isPalindrome(self, word, left, right):
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True
