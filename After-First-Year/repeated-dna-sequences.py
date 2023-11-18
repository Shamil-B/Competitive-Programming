class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        res = []
        dic = {}
        sq = ""

        for i in range(n+1):
            if i<10 and i<n:

                sq += s[i]

            elif i==10 and i<n:
                dic[sq] = i
                sq = sq[1:]
                sq += s[i]

            else:
                if sq in dic and sq not in res:
                    res.append(sq)
                if i==n:
                    return res
                dic[sq] = i
                sq = sq[1:]
                sq += s[i]


