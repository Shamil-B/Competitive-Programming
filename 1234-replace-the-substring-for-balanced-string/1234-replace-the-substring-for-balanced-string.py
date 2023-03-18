class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n//4
        dic = {'Q':0,'W':0,'E':0,'R':0}

        for c in s:
            dic[c] += 1

        if dic['Q'] == target and dic['W'] == target and dic['E'] == target and dic['R'] == target:
            return 0
        val = n
        i = 0

        for j in range(n):
            dic[s[j]] -= 1
            while i < n and dic['Q'] <= target and dic['W'] <= target and dic['E'] <= target and dic['R'] <= target:
                val = min(val, j-i+1)
                dic[s[i]] += 1
                i += 1
        return val