class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        size1 = len(str1)
        size2 = len(str2)
        
        # Initialize a 2D DP table to store the length of the shortest common supersequence.
        dp = [[0] * (size2 + 1) for _ in range(size1 + 1)]
        
        # Fill in the DP table using bottom-up dynamic programming.
        for i in range(1, size1 + 1):
            for j in range(1, size2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Reconstruct the shortest common supersequence using the DP table.
        i, j = size1, size2
        superseq = []
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                superseq.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                superseq.append(str1[i - 1])
                i -= 1
            else:
                superseq.append(str2[j - 1])
                j -= 1
        
        # Add any remaining characters from str1 and str2 to the supersequence.
        while i > 0:
            superseq.append(str1[i - 1])
            i -= 1
        while j > 0:
            superseq.append(str2[j - 1])
            j -= 1
        
        # Reverse the supersequence and convert it to a string.
        return ''.join(reversed(superseq))
