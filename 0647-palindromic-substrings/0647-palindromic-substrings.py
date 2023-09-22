class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            for j in range(i,n):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    count += 1
                    max_length =  len(substring)

        return count