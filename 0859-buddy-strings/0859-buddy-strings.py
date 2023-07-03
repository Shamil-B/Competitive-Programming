class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        count = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                count += 1
                
        if count == 2 and Counter(s) == Counter(goal):
            return True
        
        if count == 0 and len(set(s)) != len(s):
            return True 
        
        return False