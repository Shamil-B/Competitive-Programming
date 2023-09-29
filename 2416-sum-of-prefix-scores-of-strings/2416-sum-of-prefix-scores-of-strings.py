class TrieNode:
    def __init__(self):
        self.count = 0
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
            current.count += 1

    def search(self, word):
        current = self.root
        sum_ = 0
        for ch in word:
            charIndex = ord(ch)-ord('a')
            current = current.children[charIndex]
            sum_ += current.count
            if not current:
                return False

        return sum_

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        size = len(words)
        sumOfScores = [0]*size
        trie = Trie()
        
        for word in words:
            trie.insert(word)

        for i in range(size):
            sumOfScores[i] = trie.search(words[i])
            
        return sumOfScores
        