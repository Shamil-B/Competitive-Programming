class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        new = ''
        spaces.reverse()
        
        for i in range(n):
            if len(spaces) > 0 and i==spaces[-1]:
                new = new + ' ' + s[i]
                
                spaces.pop()
                
            else:
                new += s[i]
                
        return new