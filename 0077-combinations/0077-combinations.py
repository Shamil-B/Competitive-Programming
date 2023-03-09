class Solution:
    def combine(self, n, k) -> List[List[int]]:
        
        self.finalArr = []
        nums = [i for i in range(1, n+2)]
        
        def helper(arr,s):
            
            if s > n:
                return 

            if len(arr) == k:
                self.finalArr.append(arr[:])
                return
            arr.append(nums[s])
            helper(arr, s+1)
            arr.pop()
            helper(arr, s+1)
                
        helper([],0)
        return self.finalArr