class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        p1 = len(g)-1
        p2 = len(s)-1
        count = 0
        
        while p1 >= 0 and p2 >= 0:
            if g[p1] <= s[p2]:
                count += 1
                p2-=1
                p1-=1
                
            else:
                p1-=1
                
        return count