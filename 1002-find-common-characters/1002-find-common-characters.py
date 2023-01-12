from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = Counter(words[0])
        for i in words[1:]:
            counter &= Counter(i)
        return list(counter.elements())