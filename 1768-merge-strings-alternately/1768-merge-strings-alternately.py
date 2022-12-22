class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = ''
        size1 = len(word1)
        size2 = len(word2)
        p1 = 0
        p2 = 0
        
        while p1 < size1 and p2 < size2:
            
            result += word1[p1]
            result += word2[p2]
            p1+=1
            p2+=1
            
            
        while p1 < size1:
            result += word1[p1]
            p1+=1
            
        while p2 < size2:
            result += word2[p2]
            p2+=1
            
        return result