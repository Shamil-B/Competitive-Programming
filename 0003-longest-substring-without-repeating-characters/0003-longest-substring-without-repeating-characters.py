class Solution:
    def lengthOfLongestSubstring(self, st: str) -> int:
        maxx = 0
        n = len(st)
        p2 = 0
        s = ""
        size = 0
        dic = {}
        while True:
            if  p2!=n and st[p2] not in s:
                if p2<n:
                    s+=st[p2]
                size = len(s)
                p2+=1

            else:
                if s in dic:
                    size = dic[s]
                else:
                    size = len(s)
                dic[s] = size
                s = s[1:]
                maxx = max(size,maxx)
                if p2==n:
                    break
        


        return maxx