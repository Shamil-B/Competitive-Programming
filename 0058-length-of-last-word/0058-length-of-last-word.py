class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    
        ls = s.split(' ')
        while ls[-1]=='':
            ls.pop()
        return len(ls[-1])