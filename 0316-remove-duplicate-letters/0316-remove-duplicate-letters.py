class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()
        dic = {}

        for i in range(len(s)):
            dic[s[i]] = i

        for i in range(len(s)):

            if s[i] not in visited:
                while (stack and stack[-1] > s[i] and dic[stack[-1]] > i):
                    visited.remove(stack.pop())

                stack.append(s[i])
                visited.add(s[i])

        res =  ''.join(stack)
        return res