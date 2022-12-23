class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        pdt = '0'  #final product holder
        
        #what we are basically going to do is simulate the technique of multiplying two numbers by hand
        
        for i in range(len(num1)-1,-1,-1):  #iterating through both numbers backwards
            tmp = '0'*(len(num1)-i-1)
            rem = 0
            
            for j in range(len(num2)-1,-1,-1):
                res = (int(num1[i])*int(num2[j])+rem)
                rem = 0
                
                if j==0:
                    tmp = str(res) + tmp
                    
                else:
                    tmp = str(res)[-1] + tmp
                
                if res//10 != 0:
                    rem = int(str(res)[0])
                    
            pdt = str(int(pdt)+int(tmp))

        return pdt
                
        
        