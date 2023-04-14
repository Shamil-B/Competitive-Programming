class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = collections.Counter(deck)
        min_ = min(list(counter.values()))
        
        if min_ <= 1:
            return False

        for i in range(min_+1,1,-1):
            res = all(value % i ==0 for value in counter.values())

            if res: 
                return True

        return False        