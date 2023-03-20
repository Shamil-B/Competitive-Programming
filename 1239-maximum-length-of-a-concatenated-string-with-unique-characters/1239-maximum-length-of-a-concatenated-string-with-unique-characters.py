class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        newArr = []
        
        for s in arr:
            if len(s)==len(set(s)):
                newArr.append(s)
                
        alpha = {chr(i+97):0 for i in range(26)}
        self.maxx = 0
        def backtrack(path,ind,size):

            for i in range(ind,len(newArr)):
                s = newArr[i]
                cont = False
                curStr = newArr[i]
                for ch in curStr:
                    if alpha[ch] != 0:
                        cont = True
                        break
                        
                if cont:
                    continue
                    
                path.append(s)
                for ch in s:
                    alpha[ch] = 1
                    
                size = size+len(s)
                self.maxx = max(self.maxx,size)
                backtrack(path[:],i+1,size)
                path.pop()
                size -= len(s)
                
                for ch in s:
                    alpha[ch] = 0
                    
                    
        backtrack([],0,0)
        return self.maxx
        
        