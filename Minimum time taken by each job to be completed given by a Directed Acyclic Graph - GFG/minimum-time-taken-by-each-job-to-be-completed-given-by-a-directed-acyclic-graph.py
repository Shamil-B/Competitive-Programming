from typing import List
from collections import deque
from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # construct the graph first where nodes are courses and their childs being courses that are required by them
        
        prerequisite = {}
        graph = {}
        for pre,job in edges:
            if job not in prerequisite:
                prerequisite[job] = 1

            else:
                prerequisite[job] += 1
            
            if pre not in graph:
                graph[pre] = [job]

            else:
                graph[pre].append(job)
                
        starters = []
        for i in range(1,n+1):
            if i not in prerequisite:
                starters.append((i,1))
                
        jobs = deque(starters)
        finArr = [1 for i in range(n)]
        # topologicalSortingArr = []
        
        while jobs:
            curJob,level = jobs.popleft()
            # topologicalSortingArr.append(curJob)
            finArr[curJob-1] = level
            if curJob in graph:
                for consecJobs in graph[curJob]:
                    prerequisite[consecJobs] -= 1
                    if prerequisite[consecJobs] == 0:
                        jobs.append((consecJobs,level+1))
                  
        return ' '.join(list(map(str,finArr)))
       
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends