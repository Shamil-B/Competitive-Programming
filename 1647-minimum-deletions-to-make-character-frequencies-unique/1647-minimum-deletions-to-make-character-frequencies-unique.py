class Solution:
    def minDeletions(self, s: str) -> int:
        dic = Counter(s)
        
        used = set()
        vals = list(dic.values())
        vals.sort(reverse=True)
        ans = 0
        for freq in vals:
            while freq in used and freq > 0:
                freq -= 1
                ans += 1
                
            used.add(freq)
            
        return ans