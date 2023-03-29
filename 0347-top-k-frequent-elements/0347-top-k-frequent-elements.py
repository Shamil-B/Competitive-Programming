class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_ = max(nums)
        min_ = min(nums)
        range_ = [0 for i in range(max_-min_+1)]
        res = []
        
        for num in nums:
            range_[num-min_] += 1
                    
        for i in range(len(range_)):
            range_[i] = (range_[i],i+min_)
            
        range_.sort()
        
        for i in range(len(range_)-1,len(range_)-k-1,-1):
            res.append(range_[i][1])
            
        return res
            
            