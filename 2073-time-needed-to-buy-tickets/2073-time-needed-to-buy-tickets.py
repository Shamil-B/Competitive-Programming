class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        time = 0
        i = 0
        n = len(tickets)
        while tickets[k]!=0:
            ind = i%n
            if tickets[ind] != 0:
                tickets[ind] -= 1
                time += 1
                
            i += 1

        return time