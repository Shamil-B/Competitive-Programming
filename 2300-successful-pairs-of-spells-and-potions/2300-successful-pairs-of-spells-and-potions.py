class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        n = len(potions)
        potions.sort()
        for spell in spells:
            target = ceil(success/spell)
            result.append(n-bisect_left(potions,target))
            
        return result
