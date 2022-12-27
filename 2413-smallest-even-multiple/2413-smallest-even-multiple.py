class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        while n%2 != 0:
                n += n
                
        return n
                
        