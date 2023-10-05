class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        l = 0
        r = 2
        waste = 0
        while r < n:
            if nums[l] != nums[r]:
                r += 1
                l = r - 2

            else:
                nums[r] = "_"
                waste += 1
                r += 1
        print(nums)  
        
        i = 0
        while i < n-waste:
            if nums[i] == "_":
                for j in range(i,n-1):
                    nums[j], nums[j+1]  = nums[j+1], nums[j]
                    
            else:
                i += 1

        return int(n-waste)
        