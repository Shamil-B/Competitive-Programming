class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddIndices = []
        subArrays = 0
        for ind,num in enumerate(nums):
            if num%2!=0:
                oddIndices.append(ind)
                
        left = 0
        right = k-1
        size = len(oddIndices)
        
        while right<size:
            if right == size-1:
                m = len(nums)-oddIndices[right]-1
            else:
                m = oddIndices[right+1]-oddIndices[right]-1
                
            n = oddIndices[left]-oddIndices[left-1]-1 if left>0 else oddIndices[left]
            
            res = m*n + m + n + 1
            subArrays += res
            
            right += 1
            left += 1
            
        return subArrays