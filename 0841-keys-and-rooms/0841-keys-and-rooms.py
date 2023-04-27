class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()

        q = deque([0])
        while q:
            room = q.popleft()
            if room in visited:
                continue
                
            visited.add(room)
            for neigRoom in rooms[room]:
                q.append(neigRoom)

        return len(visited) == len(rooms)