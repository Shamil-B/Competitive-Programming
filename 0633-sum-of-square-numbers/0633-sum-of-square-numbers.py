class Solution:
    def judgeSquareSum(self, c: int) -> bool:        
        ptr1 = 0
        ptr2 = int(math.sqrt(c))
        
        while ptr1 <= ptr2:
            
            if ptr1**2 + ptr2**2 == c:
                return True
            
            elif ptr1**2 + ptr2**2 < c:
                ptr1 += 1
                
            else:
                ptr2 -= 1
                
        return False