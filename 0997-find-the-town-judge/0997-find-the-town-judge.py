class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustGraph = {}
        ppl = {}
        for t in trust:
            if t[1] not in ppl:
                ppl[t[1]] = 1
                
            else:
                ppl[t[1]] += 1

            if t[0] not in trustGraph:
                trustGraph[t[0]] = [t[1]]

            else:
                trustGraph[t[0]].append(t[1])

        for i in range(1,n+1):
            if i not in trustGraph and ((i in ppl and ppl[i] == n-1) or n==1 and not ppl):
                return i
            
        return -1