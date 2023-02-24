class Solution:    
    def findAnagrams(self, s,p):
        if len(s) < len(p):
            return []
        def toIdx(c):
            return ord(c) - ord('a')
        remaining = 0  
        freqP = [0]*26 
        freqS = [0]*26 
        
        for i in range(len(p)):
            freqP[toIdx(p[i])] += 1
            freqS[toIdx(s[i])] += 1
        
        for i in range(26):
            if freqP[i] != freqS[i]:
                remaining += 1
        
        winSize = len(p)
        n = len(s) - winSize + 1
        res = []
        if remaining == 0:
            res += [0]
        
        for i in range(1, n):
            removed = toIdx(s[i-1])
            added = toIdx(s[i+winSize-1]) 
            if freqS[removed] == freqP[removed]:
                remaining += 1
            freqS[removed] -= 1
            if freqS[removed] == freqP[removed]:
                remaining -= 1
            
            if freqS[added] == freqP[added]:
                remaining += 1
            freqS[added] += 1
            if freqS[added] == freqP[added]:
                remaining -= 1
            
            if remaining == 0:
                res += [i]
        return res
