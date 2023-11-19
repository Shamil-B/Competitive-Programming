class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        ans = {}
        for word in words:
            val = ''.join(sorted(word))

            if val in ans:
                ans[val].append(word)
            else:
                ans[val] = [word]
        return ans.values()
