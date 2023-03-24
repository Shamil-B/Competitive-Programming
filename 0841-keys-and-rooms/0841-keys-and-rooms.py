class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        def traverseRooms(room):
            if room in visited:
                return
            
            visited.add(room)
            
            for neigRoom in rooms[room]:
                traverseRooms(neigRoom)
            
        traverseRooms(0)
        
        return len(visited) == len(rooms)