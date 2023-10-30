class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        count = 0
        for d in directions:
            
            if not stack or d == "R" or stack[-1] == "L":
                stack.append(d)
                
            else:
                if d == "L" and stack[-1] == "R":
                    count += 2
                    stack.pop()
                    while stack and stack.pop() == "R":
                        count += 1
                    stack.append("S")
                    
                elif d == "L" and stack[-1] == "S" or d == "S" and stack[-1] == "R":
                    count += 1
                    stack.pop()
                    while stack and stack.pop() == "R":
                        count += 1

                    stack.append("S")
                    
                else:
                    stack.append(d)
                    
        return count