class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n <= 2:
            if n%2==0:
                num = n
            else:
                num = n+1

            while num%n!=0:
                num += 2
                
            return num
                
        else:
            while n%2!=0:
                n+=n
                
            return n
                
        