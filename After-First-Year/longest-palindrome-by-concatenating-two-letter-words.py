class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        length = 0
        starts = defaultdict(int)

        for word in words:
            if word[1] + word[0] in starts and starts[word[1] + word[0]] > 0:
                starts[word[1] + word[0]] -= 1
                length += 4

            else:
                starts[word] += 1

        for word in starts.keys():
            if word[0] == word[1] and starts[word[0]+word[1]] > 0:
                length += 2
                break

        return length