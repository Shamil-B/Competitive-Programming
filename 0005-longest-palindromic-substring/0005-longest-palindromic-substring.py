class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        longest_palindrome = ''
        max_length =0
        
        for i in range(n):
            for j in range(i,n):
                substring = s[i:j+1]
                if substring == substring[::-1] and len(substring) >max_length:
                    longest_palindrome = substring 
                    max_length =  len(substring)

        return longest_palindrome