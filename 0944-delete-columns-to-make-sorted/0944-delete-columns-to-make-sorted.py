class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        notsorted = 0
        
        for col in range(len(strs[0])):
            for row in range(1,len(strs)):
                if strs[row][col] < strs[row-1][col]:
                    notsorted += 1
                    break
                    
        return notsorted