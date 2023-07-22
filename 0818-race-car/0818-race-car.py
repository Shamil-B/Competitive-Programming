class Solution:
    def racecar(self, target: int) -> int:  
        # choose either A or R and return when u get to target
        # the first to get there is the answer
        
        position = 0
        speed = 1
        inst = ""
        q = deque([(position,speed,inst)])
        visited = set()
        
        while q:
            position, speed, inst = q.popleft()

            if position == target:
                return len(inst)
            
            if (position,speed) in visited:
                continue
                
            visited.add((position,speed))

            q.append((position+speed, speed*2, inst+"A"))

            q.append((position, (speed//abs(speed))*-1, inst+"R"))