class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        def getLength(target):
            start = end = -1
            for index, num in enumerate(nums):
                if num == target:
                    end = index
                    if start == -1:
                        start = index
            return end - start + 1
        
        freqToElement = defaultdict(list)
        freq = Counter(nums)
        
        for num, frq in freq.items():
            freqToElement[frq].append(num)
            
        maxFreq = max(list(freqToElement.keys()))
        
        minLength = len(nums)
        for num in freqToElement[maxFreq]:
            length = getLength(num)
            if length < minLength:
                minLength = length
                
        return minLength