class Solution:
    def checkString(self, s: str) -> bool:
        ind1 = -1
        ind2 = len(s)
        
        for ind,ch in enumerate(s):
            if ch == "a":
                ind1 = ind
                
            elif ind2 == len(s) and ch == "b":
                ind2 = ind
                
        return (ind2 > ind1)
                
            