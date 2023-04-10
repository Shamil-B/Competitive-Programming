"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {}
        importance = {}
        for emp in employees:
            graph[emp.id] = emp.subordinates
            importance[emp.id] = emp.importance

        def dfs(curEmpId,visited=None):
            for emp in employees:
                if emp.id==curEmpId:
                    break

            if not visited:
                visited = set()

            visited.add(curEmpId)
            impSum = 0
            for sub in graph[curEmpId]:
                if sub not in visited:
                    impSum += dfs(sub,visited)

            return importance[curEmpId]+impSum
        
        for emp in employees:
            if emp.id==id:
                break
                
        return dfs(emp.id)