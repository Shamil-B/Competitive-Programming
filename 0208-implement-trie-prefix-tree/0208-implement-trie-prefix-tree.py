class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None for i in range(26)]
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for ch in word:
            charIndex = ord(ch)-ord('a')
            if not current.children[charIndex]:
                current.children[charIndex] = TrieNode()
            current = current.children[charIndex]

        current.isEnd = True
   
    def search(self, word):
        current = self.root
        for ch in word:
            charIndex = ord(ch)-ord('a')
            current = current.children[charIndex]
            if not current:
                return False

        return current.isEnd

    def startsWith(self, prefix):
        current = self.root
        for ch in prefix:
            charIndex = ord(ch)-ord('a')
            current = current.children[charIndex]
            if not current:
                return False

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)