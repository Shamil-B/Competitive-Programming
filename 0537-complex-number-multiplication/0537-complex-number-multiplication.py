class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        ind1 =  num1.index('+')
        ind2 =  num2.index('+')
        
        real1 = int(num1[:ind1])
        real2 = int(num2[:ind2])
        
        im1 = int(num1[ind1+1:-1])
        im2 = int(num2[ind2+1:-1])
        
        return str(real1*real2 - im1*im2) + "+" + str(real1*im2 + real2*im1) + "i"