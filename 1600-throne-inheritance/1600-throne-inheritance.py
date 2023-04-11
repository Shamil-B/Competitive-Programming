class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.bloodMap = {}
        self.deadPpl = set()
    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.bloodMap:
            self.bloodMap[parentName].append(childName)
        else:
            self.bloodMap[parentName] = [childName]

    def death(self, name: str) -> None:
        self.deadPpl.add(name)

    def getInheritanceOrder(self) -> List[str]:
        stack = [self.king]
        visited = set()
        curOrder = []
        
        while stack:
            person = stack.pop()
            if person in visited:
                continue
                
            visited.add(person)
            if person not in self.deadPpl:
                curOrder.append(person)
                
                
            if person not in self.bloodMap:
                self.bloodMap[person] = []
                
            children = self.bloodMap[person][:]
            children.reverse()
            for child in children:
                stack.append(child)
                
        return curOrder


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()