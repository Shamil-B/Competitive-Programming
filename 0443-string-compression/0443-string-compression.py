class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        count = 0
        pt1 = 0
        pt2 = 0
        ch = chars[pt1]
        
        s = ""
        
        while pt1 < n and pt2 < n:
            
            
            if chars[pt2] != ch:
                if pt2-pt1>0:
                    s += ch
                    if pt2-pt1>1:
                        s += str(pt2-pt1)
                    pt1 = pt2
                
                ch = chars[pt1]
            
            else:
                pt2 += 1
                
        if pt2-pt1>0:
            s += ch
            if pt2-pt1>1:
                s += str(pt2-pt1)
            pt1 = pt2
            
            
        for i in range(len(s)):
            chars[i] = s[i]
            
        return len(s)