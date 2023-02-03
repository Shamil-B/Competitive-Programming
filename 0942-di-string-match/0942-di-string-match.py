class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        maxx = n
        minn = 0
        res = []
        
        for i in range(n):
            if s[i] == "I":
                res.append(minn)
                minn += 1
                
            else:
                res.append(maxx)
                maxx -= 1
                
        res.append(minn)       
        return res