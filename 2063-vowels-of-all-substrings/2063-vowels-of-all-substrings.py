class Solution:
    def countVowels(self, word: str) -> int:
        count = 0
        n = len(word)
        for i in range(n):
            if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u":
                count += (n-i)*(i+1)

        return count