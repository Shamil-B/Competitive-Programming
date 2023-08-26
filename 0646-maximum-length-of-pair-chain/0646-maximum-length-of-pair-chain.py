class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        @cache
        def solve(ind,lastPair):
            if ind >= len(pairs):
                return 0

            choose = -inf
            if pairs[ind][0] > lastPair:
                choose = solve(ind+1,pairs[ind][1]) + 1
            notChoose = solve(ind+1,lastPair)

            return max(choose,notChoose)
        
        return solve(0,-inf)