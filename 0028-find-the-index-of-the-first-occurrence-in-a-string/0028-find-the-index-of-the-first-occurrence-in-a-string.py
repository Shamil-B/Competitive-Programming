class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        splitted = self.splitIt(haystack,len(needle))
        
        if needle in splitted:
            return splitted[needle]
        
        return -1
    
    
    def splitIt(self,string,size):
        
        index = 0
        resDic = {}
        word = ''
        
        for ind,ch in enumerate(string):
            if ind < size-1:
                word += ch
                
            elif ind == size-1:
                word += ch
                resDic[word] = index
                index += 1
                
            else:
                word += ch
                word = word[1:]
                if word not in resDic:
                    resDic[word] = index
                index += 1
                
                
        return resDic
            