class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = {}
        
        left = right = maxx = res = 0
        
        while right < len(s)+1:
            vals = letters.values()
            if vals:
                maxx = max(vals) 
            
            else:
                maxx = 0
                
            dif = (right-left)-maxx

            if dif <= k:
                res = max((right-left),res)

            if dif <= k and right<len(s):
                ch = s[right]
                if ch in letters:
                    letters[ch] += 1
                    
                else:
                    letters[ch] = 1
                
                right += 1
                                
            else:
                if right==len(s):
                    break
                if letters[s[left]]==1:
                    letters.pop(s[left])
                    
                else:
                    letters[s[left]] -= 1
                    
                left += 1
                
        return res