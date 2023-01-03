class Solution:
    def printVertically(self, s):
        ind = 0
        res = []
        i = 0
        maxx = 0
        count = 0
        numOfSpaces = {}
        
        for ch in s:
            if ch == ' ':
                maxx = max(maxx,count)
                count = 0
            else:
                count+=1
                
        maxx = max(maxx,count)
        
        while i<len(s):
            
            if s[i] == ' ' and ind<maxx:
                if ind in numOfSpaces:
                    numOfSpaces[ind] += 1

                else:
                    numOfSpaces[ind] = 1
                
                    
                ind += 1
            
            elif s[i] == ' ':
                ind = 0
                i += 1
                
            else:
                
                if ind<len(res):
                    res[ind] = res[ind] +' '*numOfSpaces[ind]+ s[i]
                    numOfSpaces[ind] = 0
                    
                else:
                    if ind in numOfSpaces:
                        res.append(' '*numOfSpaces[ind]+s[i])

                    else:
                        res.append(s[i])
                    numOfSpaces[ind] = 0
                    
                ind += 1
                
                i += 1
                
        return res
