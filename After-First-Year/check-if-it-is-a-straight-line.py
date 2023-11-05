class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if (coordinates[1][0]-coordinates[0][0])==0:
            slope = 'und'
        else:
            slope = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        
        def getSlope(i):
            if (coordinates[i][0]-coordinates[i-1][0])==0:
                slope = 'und'
            else:
                slope = (coordinates[i][1]-coordinates[i-1][1])/(coordinates[i][0]-coordinates[i-1][0])
                
            return slope
        
        for i in range(1,len(coordinates)):
            if getSlope(i)!=slope:
                return False

        return True