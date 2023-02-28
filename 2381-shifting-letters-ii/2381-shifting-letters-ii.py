class Solution:
    def shiftingLetters(self, s: str, shifts) -> str:
        letters = [0 for i in range(len(s))]
        n = len(letters)
        shifted = ""
        
        for shift in shifts:
            forward = shift[2]
            start = shift[0]
            end = shift[1]
            
            letters[start] = (letters[start]+1) if forward else (letters[start]-1)
            if end+1<n:
                letters[end+1] = (letters[end+1]-1) if forward else (letters[end+1]+1)
                
                
        for i in range(1,n):
            letters[i] += letters[i-1]
            
        for i in range(n):
            letter = letters[i] + (ord(s[i])-97)
            letter = letter%26
            shifted += chr((letter)+97)
            
            
        return shifted
            