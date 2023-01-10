class Solution:
    def strStr(self, haystack: str, needle: str) -> int:        
        size = len(needle)
        word = ''
        
        for ind,ch in enumerate(haystack):
            if ind < size-1:
                word += ch
                
            elif ind == size-1:
                word += ch
                if word == needle:
                    return 0
                
                
            else:
                word += ch
                word = word[1:]
                if word == needle:
                    return ind - size + 1
                                
                
        return -1
            