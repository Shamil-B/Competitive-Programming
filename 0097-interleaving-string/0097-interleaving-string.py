class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        size1 = len(s1)
        size2 = len(s2)
        
        if size1+size2 != len(s3):
            return False

        @cache
        def solve(p1,p2,word):
            if word == s3:
                return True
            
            if (word != s3[:len(word)]) or (p1 >= size1 and p2 >= size2):
                return False
            
            if p1 >= size1:
                return solve(p1,p2+1,word + s2[p2])
            
            if p2 >= size2:
                return solve(p1+1,p2,word + s1[p1])
            
            word1 = word + s1[p1]
            word2 = word + s2[p2]
            
            return solve(p1+1,p2,word1) or solve(p1,p2+1,word2)
        
        return solve(0,0,"")