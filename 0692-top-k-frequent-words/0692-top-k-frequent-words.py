class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        newFreq = {}

        for item in freq.items():
            if item[1] in newFreq:
                newFreq[item[1]].append(item[0])
                
            else:
                newFreq[item[1]] = [item[0]]
                
        limit = 2*k
        for key in newFreq.keys():
            newFreq[key] = sorted(newFreq[key])
        newFreq = list(newFreq.items())
        newFreq.sort(reverse=True)
        ans = []
        
        for i in range(len(newFreq)):
            for j in range(len(newFreq[i][1])):
                ans.append(newFreq[i][1][j])
                if len(ans)==k:
                    return ans