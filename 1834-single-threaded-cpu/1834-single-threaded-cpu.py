class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for ind, task in enumerate(tasks):
            tasks[ind] = (task[0],task[1],ind)
            
        tasks.sort(reverse=True)
        
        que = []
        heapq.heapify(que)
        ans = []
        time = 0
        while tasks or que:
            while tasks and (time >= tasks[-1][0]):
                tmp = tasks.pop()
                tmp = (tmp[1],tmp[0],tmp[2])
                heapq.heappush(que,tmp)

            if que:
                res = heapq.heappop(que)
                cur = [res]
                while que and res[0] == que[0][0]:
                    cur.append(heapq.heappop(que))
                
                cur.sort(key = lambda x:x[2])
                ans.append(cur[0][2])
                time += cur[0][0]
                for i in range(1,len(cur)):
                    heapq.heappush(que,cur[i])                
                
            else:
                time = tasks[-1][0]
                
        return ans