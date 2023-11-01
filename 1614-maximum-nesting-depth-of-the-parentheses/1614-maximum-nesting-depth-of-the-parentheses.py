class Solution:
    def maxDepth(self, s: str) -> int:
        stack = 0
        max_depth = 0
        
        for i in range(len(s)):
            max_depth = max(max_depth, stack)
            if s[i] == "(":
                stack += 1

            elif s[i] == ")":
                stack -= 1
                
        return max_depth