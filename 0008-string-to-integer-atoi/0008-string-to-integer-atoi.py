class Solution:
    def myAtoi(self, s: str) -> int:
        
        num = ''
        prd = 1
        op = 0
        
        for ch in s:
            
                
            if (ord(ch) > 47 and ord(ch) < 58):
                num += ch
                
            elif ((ch=='-' or ch=='+' or ch==' ' or ch=='.') and (num!='' or op > 0)):
                break
                
            elif ch==' ':
                continue
                
            elif ch=='-':
                prd = -1
                op += 1
                
            elif ch=="+":
                prd = 1
                op += 1
                
                
            else:
                break
                
        if num == '' or op > 1:
            return 0
                
        res = int(num)*prd 
        
        if res > 2**31-1:
            return 2**31-1
        
        elif res < -2**31:
            return -2**31
        
        return res