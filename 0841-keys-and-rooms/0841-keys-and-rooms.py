class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()

        stack = [0]
        while stack:
            room = stack.pop()
            if room in visited:
                continue
                
            visited.add(room)
            for neigRoom in rooms[room]:
                stack.append(neigRoom)

        return len(visited) == len(rooms)