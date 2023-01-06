class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        number1 = num1.split('+')
        number2 = num2.split('+')
        
        real1 = int(number1[0])
        real2 = int(number2[0])
        
        im1 = int(number1[1][:-1])
        im2 = int(number2[1][:-1])
        
        return str(real1*real2 - im1*im2) + "+" + str(real1*im2 + real2*im1) + "i"