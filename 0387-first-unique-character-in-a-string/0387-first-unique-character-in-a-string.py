class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for ch in s:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 0
                
                
        for ind,ch in enumerate(s):
            if dic[ch]==0:
                return ind
            
        return -1
        