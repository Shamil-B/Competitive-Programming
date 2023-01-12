class Solution:
    def reverseString(self, s: List[str]) -> None:
        size = len(s)
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(size//2):
            s[i], s[size-1-i] = s[size-1-i],s[i]
            
