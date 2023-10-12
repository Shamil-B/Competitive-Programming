class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        max_radius = 0
        size = len(heaters)
        heaters.sort()
        for house_pos in houses:
            index = bisect_right(heaters, house_pos)

            if index == size:
                max_radius = max(max_radius, house_pos-heaters[index-1])
                
            elif index == 0:
                max_radius = max(max_radius, abs(house_pos-heaters[index]))

            else:
                max_radius = max(max_radius, min(house_pos-heaters[index-1], abs(house_pos-heaters[index])))
     
        return max_radius