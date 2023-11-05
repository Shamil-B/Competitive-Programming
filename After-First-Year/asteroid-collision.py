class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        size = len(asteroids)
        for i in range(size):
            if not stack:
                stack.append(asteroids[i])
                
            else:
                if asteroids[i] < 0:
                    while stack and stack[-1] > 0 and abs(asteroids[i]) > stack[-1]:
                                stack.pop()

                    if not stack or stack[-1] < 0:
                        stack.append(asteroids[i])

                    elif abs(asteroids[i]) == stack[-1]:
                        stack.pop()
                            
                else:
                    stack.append(asteroids[i])

        return stack