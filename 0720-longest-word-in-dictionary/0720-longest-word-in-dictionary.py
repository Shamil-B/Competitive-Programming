class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ind, ch in enumerate(word):
            charIndex = ord(ch)-ord('a')
            
            if not current.children[charIndex] and ind < len(word)-1:
                return False

            if not current.children[charIndex]:
                current.children[charIndex] = TrieNode()
            current = current.children[charIndex]

        return word   
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        ans = ""
        words.sort()
        for word in words:
            res = trie.insert(word)
            if res != False:
                if len(res) > len(ans):
                    ans = res
                    
                if len(res) == len(ans):
                    ans = min(ans,res)
            
        return ans
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        