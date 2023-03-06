class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.freq = {}
        self.timesSet = set(times)
        
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
        
        if t in self.times:
            return self.persons[bisect_left(self.times,t)]
        
        return self.persons[bisect_left(self.times,t)-1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)