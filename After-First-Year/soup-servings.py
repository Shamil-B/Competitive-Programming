class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1

        @cache
        def solve(soup_a, soup_b):
            if soup_a == 0 and soup_b == 0:
                return 0.5

            if soup_a == 0:
                return 1

            if soup_b == 0:
                return 0

            return 0.25 * (solve(max(0, soup_a-100), soup_b) + solve(max(0, soup_a-75), max(0, soup_b-25)) + solve(max(0, soup_a-50), max(0, soup_b-50)) + solve(max(0, soup_a-25), max(0, soup_b-75)))
        
        return solve(n, n)