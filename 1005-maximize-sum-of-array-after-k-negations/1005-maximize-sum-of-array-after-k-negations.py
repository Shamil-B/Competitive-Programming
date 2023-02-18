class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        negatives = []
        n = len(nums)
        nums.sort()
        j = 0
        
        if nums[0] < 0:
            for i in range(n):
                if nums[i]<0:
                    j = i
                    
                else:
                    break
                    
            negatives = nums[:j+1]
            if j+1<n:
                nums = nums[j+1:]
                
            else:
                nums = []
            
            for i in range(len(negatives)):
                if k==0:
                    break
                    
                negatives[i] = negatives[i]*-1
                k -= 1
                
            nums = negatives+nums
                
            nums.sort()
                
                
        for i in range(k):
            nums[0] = nums[0]*-1
                
        return sum(nums)