class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.freq = {}
        self.timesSet = set(times)
        
        
#first we modified the persons array to hold the person with maximum votes until the current index

        maxx = 0
        maxVal = persons[0]
        for ind,person in enumerate(persons):
            
            if person not in self.freq:
                self.freq[person] = 1
                
            else:
                self.freq[person] += 1
                
            if self.freq[person] >= maxx:
                maxx = self.freq[person]
                maxVal = person
                
            self.persons[ind] = maxVal

    def q(self, t: int) -> int:
        
        if t in self.timesSet:
            return self.persons[self.bisectLeft(self.times,t)]
        
        return self.persons[self.bisectLeft(self.times,t)-1]
    
    
    def bisectLeft(self,nums,target):
        n = len(nums)
        low = -1
        high = n
        
        while low+1<high:
            mid = low + (high-low)//2
            
            if nums[mid] >= target:
                high = mid
                
            else:
                low = mid

        return high
        
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)