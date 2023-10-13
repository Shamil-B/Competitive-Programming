class Solution:
    def countOrders(self, n: int) -> int:
        MOD = pow(10,9) + 7
        @cache
        def solve(p, d):
            if p < 0 or (p == 0 and d == 0):
                return 1
            
            pick_up = p*solve(p-1, d)
            delivery = 0
            
            if d > p:
                delivery = (d-p)*solve(p, d-1)
                
            return pick_up+delivery
            
        return solve(n, n)%(MOD)