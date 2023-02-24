class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log[:3]=="../":
                if stack:
                    stack.pop()

            elif log[0] != ".":
                stack.append(0)
                
        return len(stack)