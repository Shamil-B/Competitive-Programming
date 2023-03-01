class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq = [0 for i in range(26)]
        for ch in s1:
            freq[ord(ch)-97] += 1

        k = len(s1)
        left = right = 0
        n = len(s2)

        for i in range(k):
            freq[ord(s2[i])-97] -= 1

        if self.allZero(freq):
            return True
        
        right = k
        left = 0
        while right<n:
            freq[ord(s2[right])-97] -= 1
            freq[ord(s2[left])-97] += 1

            if self.allZero(freq):
                return True
            
            right += 1
            left += 1
            
            

        return False
    

    def allZero(self,arr):
        for num in arr:
            if num!=0:
                return False

        return True