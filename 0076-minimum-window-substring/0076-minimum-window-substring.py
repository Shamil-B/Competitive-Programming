class Solution:
    def minWindow(self, s: str, t: str) -> str:

            if len(t) > len(s): return ""

            minLength = len(s) + 1

            count = Counter(t)

            distincts = len(count)

            i,j = 0,0

            minI = -1
            minJ = -1


            while j < len(s):
                if s[j] in count:
                    count[s[j]] -= 1
                    if count[s[j]] == 0: distincts -= 1

                while distincts == 0:
                    if j - i + 1 < minLength:
                        minLength = j - i + 1
                        minI = i
                        minJ = j
                    if s[i] in count: 
                        count[s[i]] += 1
                        if count[s[i]] == 1 : distincts += 1

                    i += 1

                j += 1

            substring = s[minI:minJ + 1]

            return substring