class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        validPoints = {}
        size = len(points)
        min_index = None
        
        
        for i in range(size):
            
            x1 = points[i][0]
            y1 = points[i][1]
            
            if (x1 == x or y1 == y):
                
                validPoints[i] = abs(x-x1) + abs(y-y1)
                
                if min_index==None:
                    min_index = i
                
        keys = list(validPoints.keys())
        
        for i in keys:
            if validPoints[i] < validPoints[min_index]:
                min_index = i
                
                
        if min_index == None:
            return -1
        
        return min_index