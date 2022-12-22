class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        
        containerDic1 = {}
        containerDic2 = {}
        
        for ch in s:
            
            if ch not in containerDic1:
                containerDic1[ch] = 0
            
            else:
                containerDic1[ch] += 1
                
                
        for ch in t:
            
            if ch not in containerDic2:
                containerDic2[ch] = 0
            
            else:
                containerDic2[ch] += 1
                
        
            
            
        for ch in t:
            if ch not in containerDic1 or containerDic1[ch] < containerDic2[ch]:
                return ch