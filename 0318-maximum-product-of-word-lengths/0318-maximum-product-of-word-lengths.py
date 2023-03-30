class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        lens = []
        max_ = 0
        for ind in range(n):
            num = 0
            word = words[ind]
            for i in range(len(word)):
                ch = word[i]
                if not num&(1<<(ord(ch)-97)):
                    num ^= (1<<(ord(ch)-97))
                
            words[ind] = num
            lens.append(len(word))
            
        for i in range(n):
            for j in range(i+1,n):
                if (words[i]&words[j])==0:
                    max_ = max(max_,lens[i]*lens[j])
                  
        return max_