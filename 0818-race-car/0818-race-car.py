class Solution:
    def racecar(self, target: int) -> int:  
        # choose either A or R for each step and return the length of the instruction
        # when u get to target
        # the first to get there is the answer
        
        position = 0
        speed = 1
        instructionLength = 0
        q = deque([(position,speed,instructionLength)])
        visited = set()
        
        while q:
            position, speed, instructionLength = q.popleft()

            if position == target:
                return instructionLength
            
            if (position,speed) in visited:
                continue
                
            visited.add((position,speed))

            q.append((position+speed, speed*2, instructionLength+1))
            
            speed = -1 if speed > 0 else 1
            q.append((position, speed, instructionLength+1))