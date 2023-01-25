class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        ans = []
        for ind,ch in enumerate(s):
            dic[ch] = ind

        maxx = 0
        p1 = 0

        for i in range(len(s)):
            if dic[s[i]]>maxx:
                maxx = dic[s[i]]
            if maxx==i:
                ans.append(i-p1+1)
                p1 = i+1

        return ans