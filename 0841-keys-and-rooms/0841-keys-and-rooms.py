class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        roomMap = {}
        for i in range(n):
            roomMap[i] = rooms[i]
          
        visited = set()
        def traverseRooms(room):
            if room in visited:
                return
            
            visited.add(room)
            
            for neigRoom in roomMap[room]:
                traverseRooms(neigRoom)
            
        traverseRooms(0)
        
        return len(visited) == len(rooms)