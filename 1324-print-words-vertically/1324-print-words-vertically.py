class Solution:
    def printVertically(self, s):
        ind = 0
        res = []
        i = 0
        maxx = 0
        count = 0
        flag = {}
        
        for ch in s:
            if ch == ' ':
                maxx = max(maxx,count)
                count = 0
            else:
                count+=1
                
        maxx = max(maxx,count)
        
        while i<len(s):
            
            if s[i] == ' ' and ind<maxx:
                if ind in flag:
                    flag[ind] += 1

                else:
                    flag[ind] = 1
                
                    
                ind += 1
            
            elif s[i] == ' ':
                ind = 0
                i += 1
                
            else:
                
                if ind<len(res):
                    res[ind] = res[ind] +' '*flag[ind]+ s[i]
                    flag[ind] = 0
                    
                else:
                    if ind in flag:
                        res.append(' '*flag[ind]+s[i])

                    else:
                        res.append(s[i])
                    flag[ind] = 0
                    
                ind += 1
                
                i += 1
                
        return res
