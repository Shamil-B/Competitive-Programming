class UnionFind:
    def __init__(self, elements):
        self.reps = elements
        self.size = {}

        for key in elements.keys():
            self.size[key] = 1

    def findRep(self,x):
        rep = self.reps[x]

        while rep!=self.reps[rep]:
            rep = self.reps[rep]

        topParent = rep
        rep = self.reps[x]
        
        while rep!=self.reps[rep]:
            temp = rep
            rep = self.reps[rep]
            self.reps[temp] = topParent
            
        return topParent
    
    def union(self,x,y):
        oldRep = self.findRep(x)
        newRep = self.findRep(y)

        size_1 = self.size[oldRep]
        size_2 = self.size[newRep]

        new_size = size_1 + size_2

        if size_1 > size_2:
            newRep, oldRep = oldRep,newRep

        self.size[newRep] = new_size
        self.size[oldRep] = new_size

        self.reps[oldRep] = newRep
        
    def connected(self,x,y):
        return self.findRep(x) == self.findRep(y)


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def is_inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) 
        
        rows = len(grid)
        cols = len(grid[0])
        elements = {}
        zero_found = False
        one_found = False
        
        neighbours = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        for row in range(rows):
            for col in range(cols):
                element = (row, col)
                elements[element] = element
                if not zero_found and not grid[row][col]:
                    zero_found = True
                    
                if not one_found and grid[row][col]:
                    one_found = True
                    
                

        uf = UnionFind(elements)
        for row in range(rows):
            for col in range(cols):
                cell = (row, col)
                if grid[row][col]:
                    for r, c in neighbours:
                        neig = (row+r, col+c)
                        if is_inbound(neig[0], neig[1]) and grid[neig[0]][neig[1]] and not uf.connected(cell, neig):
                            uf.union(cell, neig)

        max_size = max(list(uf.size.values()))
        if zero_found and one_found:
            max_size += 1

        for row in range(rows):
            for col in range(cols):
                cell = (row, col)
                neighs = []
                if not grid[row][col]:
                    for r, c in neighbours:
                        neig = (row+r, col+c)
                        if is_inbound(neig[0], neig[1]) and grid[neig[0]][neig[1]]:
                            neighs.append(neig)
                            
                sum_ = 1
                used = set()
                for i in range(len(neighs)):
                    neig = uf.findRep(neighs[i])
                    if neig not in used:
                        sum_ += uf.size[neig]
                        used.add(neig)
                        
                max_size = max(max_size, sum_)
                            
        return max_size