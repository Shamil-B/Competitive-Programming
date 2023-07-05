class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(set(nums)) == 1:
            return 1

        if len(nums) == 2:
            if nums[0] != nums[1]:
                return 2
            return 1

        max_ = min_ = nums[0]
        diff = nums[1]
        i = 2
        while nums[0] == diff:
            diff = nums[i]
            i += 1

        inc = diff>nums[0]
        count = 1
        for index, num in enumerate(nums[1:]):
            if inc:
                if num > min_:
                    min_ = max_ = num
                    count += 1
                    inc = False
                    
                else:
                    min_ = min(min_,num)
                
            else:
                
                if num < max_:
                    min_ = max_ = num
                    count += 1
                    inc = True
                    
                else:
                    max_ = max(max_,num)
                    
                    
        return count