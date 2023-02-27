class Solution:
    def checkString(self, s: str) -> bool:
        s2 = sorted(list(s))
        return s2==list(s)