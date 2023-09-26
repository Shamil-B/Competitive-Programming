class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for ch in word:
            charInd = ord(ch)-ord('a')
            if not current.children[charInd]:
                current.children[charInd] = TrieNode()
            current = current.children[charInd]
            
        current.isEnd = True
    def search(self, word: str) -> bool:
        current = self.root       
        for ind, ch in enumerate(word):
            res = False
            if ch == ".":
                for index, child in enumerate(current.children):
                    if child:
                        if self.search(word[:ind]+chr(ord('a')+index)+word[ind+1:]):
                            return True
                return False

            charInd = ord(ch)-ord('a')
            current = current.children[charInd]
            if not current:
                return False
            
        return current.isEnd
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)