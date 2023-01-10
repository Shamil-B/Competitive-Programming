class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return self.splitIt(haystack,needle)
        
    
    def splitIt(self,string,needle):
        size = len(needle)
        
        index = 0
        resDic = {}
        word = ''
        
        for ind,ch in enumerate(string):
            if ind < size-1:
                word += ch
                
            elif ind == size-1:
                word += ch
                index += 1
                if word == needle:
                    return 0
                
                
            else:
                word += ch
                word = word[1:]
                if word == needle:
                        return index
                
                index += 1
                
                
        return -1
            