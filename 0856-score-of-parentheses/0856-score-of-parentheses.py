class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        res = ""
        score = 0
        for ch in s:
            if ch == "(":
                stack.append(ch)
                
            else:
                stack.pop()
                
            res += ch
                
            if not stack:
                score += self.helper(res)
                res = ""
                
        return score
        
        
    def helper(self,s):
        if s=="()":
            return 1
        
        else:
            return 2*self.scoreOfParentheses(s[1:-1])
        
        