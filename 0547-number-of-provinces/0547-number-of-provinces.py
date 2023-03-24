class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        routes = {}
        n = len(isConnected)
        provinces = 0
        for rowInd in range(1,n+1):
            routes[rowInd] = []
            row = isConnected[rowInd-1]

            for ind in range(n):
                if ind != rowInd-1 and row[ind] == 1:
                    routes[rowInd].append(ind+1)
                    
        explored = set()
        for city in routes.keys():
            if self.explore(city,routes,explored):
                provinces += 1
                
        return provinces
                
    def explore(self,city,routes,visited):
        
        if city in visited:
            return False
        
        visited.add(city)
        
        for otherCity in routes[city]:
            self.explore(otherCity,routes,visited)
            
        return True
        