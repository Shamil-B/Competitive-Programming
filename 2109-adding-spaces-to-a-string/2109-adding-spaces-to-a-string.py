class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        size1 = len(s)
        new = ''
        spaces.reverse()
        size2 = len(spaces)-1
        
        for i in range(size1):
            
            if size2 >= 0 and i == spaces[size2]:
                new = new + ' ' + s[i]
                size2 -= 1 
                
            else:
                new += s[i]
                
        return new