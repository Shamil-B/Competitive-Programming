class Solution:
    def hammingWeight(self, n: int) -> int:
        if n<2:
            return n
        
        rem = n%2
        return self.hammingWeight(n//2) + rem