class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        swap = True
        
        while swap:
            swap = False
            for index in range(len(names)-1):
                if heights[index] < heights[index+1]:
                    heights[index] , heights[index+1] = heights[index+1], heights[index]
                    names[index] , names[index+1] = names[index+1], names[index]
                    swap = True
                    
        return names