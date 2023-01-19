class Solution:
    def romanToInt(self, s: str) -> int:
        dic1 = {
                "IV":4,
                "IX":9,
                "XL":40,
                "XC":90,
                "CD":400,
                "CM":900
               }
        
        dic2 = {
                "I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000
        }
        
        i = 0
        num = 0
        
        while i<len(s):
            key = s[i:i+2]
            if key in dic1:
                num += dic1[key]
                i += 2
                
            else:
                num += dic2[s[i]]
                i += 1
                
        return num
                