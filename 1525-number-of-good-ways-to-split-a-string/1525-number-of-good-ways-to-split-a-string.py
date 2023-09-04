class Solution:
    def numSplits(self, s: str) -> int: 
        goodSplits = 0
        leftDic = defaultdict(int)
        rightDic = defaultdict(int)
        
        leftDic[s[0]] = 1
        rightDic = Counter(s)
        rightDic[s[0]] -= 1
        size1 = 1
        size2 = len(set(s[1:]))
        for i in range(1,len(s)):
            if size1 == size2:
                goodSplits += 1

            if leftDic[s[i]] == 0:
                size1 += 1

            leftDic[s[i]] += 1

            if rightDic[s[i]] == 1:
                size2 -= 1

            rightDic[s[i]] -= 1
            

        return goodSplits