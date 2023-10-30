class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        size = len(asteroids)
        for i in range(size):
            if mass < asteroids[i]:
                return False
            
            mass += asteroids[i]
            
        return True