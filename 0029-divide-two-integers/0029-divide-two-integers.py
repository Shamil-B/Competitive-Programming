class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = dividend//divisor
        
        if res > 2**31 - 1:
            return 2**31 - 1
        
        if res < -2**31:
            return -2**31
        
        if dividend*divisor < 0 and res != dividend/divisor:
            return res + 1
        return res