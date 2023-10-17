class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        dic = {}
        for person, pref in enumerate(preferences):
            dic[person] = {}
            for index, other_person in enumerate(pref):
                dic[person][other_person] = index
                
        unhappy_friends = set()
        for x, y in pairs:
            for u, v in pairs:
                if x != u or y != v:
                    if (dic[x][u] < dic[x][y] and dic[u][x] < dic[u][v]) or ((dic[x][v] < dic[x][y] and dic[v][x] < dic[v][u])):
                        unhappy_friends.add(x)
                        
                    if (dic[y][u] < dic[y][x] and dic[u][y] < dic[u][v]) or ((dic[y][v] < dic[y][x] and dic[v][y] < dic[v][u])):
                        unhappy_friends.add(y)
                       
        return len(unhappy_friends)