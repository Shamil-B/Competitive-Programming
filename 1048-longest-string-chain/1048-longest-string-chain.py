class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        size = len(words)  
        words.sort(key=lambda x : len(x))
        memo = {}
        def isPred(word1,word2):
            concat = word1+word2
            if concat in memo:
                return memo[concat]

            p1 = p2 = 0
            once = 1
            if len(word2)-len(word1) != 1:
                return False

            for i in range(len(word1)):
                if word1[p1] != word2[p2]:
                    if once == 0:
                        memo[concat] = False
                        return False
                    once -= 1
                    p2 += 1
  
                else:
                    p1 += 1
                    p2 += 1
            if once < 1 and word2[p2] != word1[p1]:
                memo[concat] = False
                return False
            
            memo[concat] = True
            return True
            
        @cache
        def solveTopDown(ind):
            max_ = 1
            for i in range(ind+1,size):
                if isPred(words[ind],words[i]):
                    max_ = max(max_,solveTopDown(i)+1) 
     
            return max_
        
#         max_ = 1
#         for i in range(size):
#             max_ = max(max_,solveTopDown(i))
            
#         return max_
    
        def solveBottomUp():
            dp = [0]*size
            for i in range(size-1,-1,-1):
                for j in range(i-1,-1,-1):
                    if isPred(words[j],words[i]):
                        dp[j] = max(dp[j],dp[i]+1)
            return max(dp) + 1
        
        return solveBottomUp()

            