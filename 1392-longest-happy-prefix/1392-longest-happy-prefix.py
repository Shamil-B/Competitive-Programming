class Solution:
    def longestPrefix(self, s: str) -> str:
        alpha = 27
        size = len(s)
        hashes = []
        MOD = pow(10, 9) + 7
        for i in range(size):
            hashes.append(pow(alpha, i, MOD))

        def addLast(wordHash, newCh):
            return (wordHash*alpha + (ord(newCh)-ord('a')+1)) % MOD

        def addFirst(wordHash, firstCh, oldLength):
            return (wordHash + (ord(firstCh)-ord('a')+1)*hashes[oldLength-1]) % MOD

        set_ = set()
        starting_index = -1
        current_hash = 0
        for i in range(len(s)-1):
            current_hash = addLast(current_hash, s[i])
            set_.add(current_hash)

        current_hash = 0
        for i in range(len(s)-1,-1,-1):
            current_hash = addFirst(current_hash, s[i], len(s)-i)

            if current_hash in set_ and s[:len(s)-i] == s[i:]:
                starting_index = i

        return s[starting_index:] if starting_index != -1 else ""