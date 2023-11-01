class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0
        
        for i in range(len(s)):
            max_depth = max(max_depth, len(stack))
            if s[i] == "(":
                stack.append("(")

            elif s[i] == ")":
                stack.pop()
                
        return max_depth