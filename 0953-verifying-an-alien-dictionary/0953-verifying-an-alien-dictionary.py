class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        size = len(words)
        orderDic = {}
        
        for ind,ch in enumerate(order):
            orderDic[ch] = ind
            
        print(orderDic)
        
        for index1 in range(size-1):
            if not self.compare(words[index1],words[index1+1],orderDic):
                return False

        return True
    
    
    
    def compare(self,word1,word2,orderDic):
        size1 = len(word1)
        size2 = len(word2)
        
        for i in range(min(size1,size2)):
            
            if orderDic[word1[i]] > orderDic[word2[i]]:
                return False
            
            elif orderDic[word1[i]] < orderDic[word2[i]]:
                return True
            
        if size1>size2:
            return False
            
            
        return True
        
        