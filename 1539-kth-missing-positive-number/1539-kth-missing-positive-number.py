class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        sett = set(arr)
        i = 1
        while True:
            if k == 0:
                return lastMissing

            if i not in sett:
                k -= 1
                lastMissing = i
                
            i += 1

