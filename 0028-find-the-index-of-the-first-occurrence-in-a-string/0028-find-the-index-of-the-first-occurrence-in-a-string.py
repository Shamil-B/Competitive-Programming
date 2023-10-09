class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        alpha = 27
        size1 = len(haystack)
        size2 = len(needle)
        size = max(len(haystack),len(needle))
        hashes = []

        for i in range(size):
            hashes.append(pow(alpha,i))
            
        def addLast(wordHash, newCh):
            return wordHash*alpha + (ord(newCh)-ord('a')+1)

        def pollFirst(wordHash, firstCh, oldLength):
            return wordHash - (ord(firstCh)-ord('a')+1)*hashes[oldLength-1]

        def compareHash(hash1, hash2):
            return hash1 == hash2

        def solve(word, target):
            targetHash = 0
            for ch in target:
                targetHash = addLast(targetHash, ch)

            currentHash = 0
            for ch in word[:size2]:
                currentHash = addLast(currentHash, ch)

            window_size = size2
            for i in range(size1):
                if compareHash(currentHash, targetHash):
                    return i

                if i+window_size < size1 and i < size1:
                    currentHash = pollFirst(currentHash, word[i], size2)
                    currentHash = addLast(currentHash, word[i + window_size])

            return -1
        
        return solve(haystack, needle)
