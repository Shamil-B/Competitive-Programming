class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # come from both sides
        # if the same decrement both
        # if different explore both and return max
        # base case if left >= right
        
        @cache
        def solve(l,r):
            if l == r:
                return 1
            
            if l > r:
                return 0
            
            if s[l] == s[r]:
                return solve(l+1,r-1) + 2
            
            else:
                return max(solve(l+1,r),solve(l,r-1))
            
        return solve(0,len(s)-1)
            
            