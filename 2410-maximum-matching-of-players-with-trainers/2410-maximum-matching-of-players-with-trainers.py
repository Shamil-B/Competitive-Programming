class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        n = len(players)
        m = len(trainers)
        p1 = p2 = match = 0
        
        while p1 < n and p2 < m:
            if players[p1] <= trainers[p2]:
                match += 1
                p1 += 1
                p2 += 1
                
            else:
                p2 += 1
                
        return match