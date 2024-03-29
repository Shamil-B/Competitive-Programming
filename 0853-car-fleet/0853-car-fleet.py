class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos_speed = sorted(zip(position, speed), reverse=True)
        
        arrivals = [(target - position) * (1/speed) for position, speed in pos_speed]
        
        fleets = len(position)
        
        for idx, time in enumerate(arrivals[1:]):
            
             if time <= arrivals[idx]:
                fleets -= 1
                arrivals[idx+1] = arrivals[idx]
        return fleets