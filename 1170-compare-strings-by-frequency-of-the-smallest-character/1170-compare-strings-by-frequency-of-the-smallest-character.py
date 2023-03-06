class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res = []
        words_freq = []
        n = len(words)
        for word in words:
            words_freq.append(self.f(word))
            
        words_freq.sort()
        for i in range(len(queries)):
            q = queries[i]
            freq = self.f(q)
            res.append(n-bisect_right(words_freq,freq))
        
        return res

    def f(self,s):
        min_freq = 0
        minn = "z"
        
        for ch in s:
            if ch<minn:
                minn = ch
                
        for ch in s:
            if ch==minn:
                min_freq += 1
                
        return min_freq