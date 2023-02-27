class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        rem = 0
        res = ""
        p1 = n-1
        p2 = m-1

        while p1 >= 0 and p2 >= 0:
            summ = int(num1[p1]) + int(num2[p2]) + rem
            rem = summ//10
            summ = summ%10
            
            res = str(summ) + res
            p1 -= 1
            p2 -= 1
            
        while p1 >= 0:
            summ = int(num1[p1]) + rem
            rem = summ//10
            summ = summ%10
            
            res = str(summ) + res
            p1 -= 1
            
        while p2 >= 0:
            summ = int(num2[p2]) + rem
            rem = summ//10
            summ = summ%10
            
            res = str(summ) + res
            p2 -= 1
            
        if rem!=0:
            res = str(rem)+res
            
        return res
            
    