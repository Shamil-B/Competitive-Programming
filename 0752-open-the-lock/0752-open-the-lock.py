class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque([('0000',0)])
        visited = set()
        dead = set(deadends)
        level = 0
        
        if '0000' in dead:
            return -1

        while q:
            node,level = q.popleft()
            
            if node==target:
                return level
            
            if node in visited:
                continue
                
            visited.add(node)

            for ind in range(4):
                ls = list(node)
                ls[ind] = str((int(node[ind])+1)%10)
                val1 = ''.join(ls)

                if val1 not in dead:
                    q.append((val1,level+1))


                ls = list(node)
                ls[ind] = str((int(node[ind])-1)%10)
                val2 = ''.join(ls)

                if val2 not in dead:
                    q.append((val2,level+1))


   
        return -1