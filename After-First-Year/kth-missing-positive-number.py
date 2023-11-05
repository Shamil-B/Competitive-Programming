class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        sett = set(arr)
        num = 1
        while True:
            if k == 0:
                return lastMissing

            if num not in sett:
                k -= 1
                lastMissing = num
                
            num += 1

