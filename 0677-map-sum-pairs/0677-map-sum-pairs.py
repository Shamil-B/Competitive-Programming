class TrieNode:

    def __init__(self):
        self.isEnd = False
        self.children = [None for i in range(26)]
        
        
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.sum_ = defaultdict(int)
        self.used = {}

    def insert(self, key: str, val: int) -> None:
        word = key
        if word in self.used:
            tmp = val
            val -= self.used[word]
            self.used[word] = tmp

        else:
            self.used[word] = val

        current = self.root
        for ind, ch in enumerate(word):
            charIndex = ord(ch)-ord('a')
            if not current.children[charIndex]:
                current.children[charIndex] = TrieNode()
            current = current.children[charIndex]
            self.sum_[word[:ind+1]] += val

        current.isEnd = True

    def sum(self, prefix: str) -> int:
        return self.sum_[prefix]

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)