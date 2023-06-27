class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        # three cases
        
        # without the first ele
        nums1 = nums[1:]
        
        # without the last ele
        nums2 = nums[:-1]
        
        # without both
        nums3 = nums[1:-1]
        
        memo = {}
        def dp(n,arr):

                
            if n > len(arr)-1:
                return 0

            if n == len(arr)-1:
                return arr[-1]
            
            if n == len(arr)-2:
                return max(arr[-1],arr[-2])
            
            if n not in memo:
                memo[n] = max((arr[n])+dp(n+2,arr),dp(n+1,arr))
                
            return memo[n]
        
        max1 = dp(0,nums1)
        memo = {}
        max2 = dp(0,nums2)
        memo = {}
        max3 = dp(0,nums3)

        return max(max1,max2,max3)
        