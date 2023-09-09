import sys
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        sys.set_int_max_str_digits(1000000)
        dp = {}
        count = 1
        for i in range(len(corridor)):
            if corridor[i] == "S":
                dp[count] = i
                count += 1

        if count == 1 or (count - 1) % 2:
            return 0

        answer = 1
        for i in range(2, count - 1, 2):
            answer *= (dp[i + 1] - dp[i])
            answer %= (10**9+7)
                
        return answer