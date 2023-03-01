class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = right = 0
        n = len(fruits)
        types = {}
        maxx = 0
        
        while right < n:
            if len(types) <= 2:
                if fruits[right] in types:
                    types[fruits[right]] += 1
                    
                else:
                    types[fruits[right]] = 1
                    
            if len(types) <= 2:
                maxx = max(maxx,right-left+1)
                
            while len(types) > 2:
                if types[fruits[left]] == 1:
                    types.pop(fruits[left])
                    
                else:
                    types[fruits[left]] -= 1
                    
                left += 1
                
            right += 1
            
        return maxx
                    