class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        ptr1 = 0
        ptr2 = n-1
        value = skill[0] + skill[-1]
        chemistry = 0
        
        while ptr1 < ptr2:
            if skill[ptr1] + skill[ptr2] != value:
                return -1
            
            else:
                chemistry += skill[ptr1]*skill[ptr2]
                ptr1 += 1
                ptr2 -= 1
                
        return chemistry
                