class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        nums = arr
        new = []
        while True:
            if len(nums)==0:
                return new
            max_ind  = nums.index(max(nums))
            k = max_ind + 1
            new.append(k)
            tmp1 = nums[:k]
            tmp2 = nums[k:]
            tmp1.reverse()
            nums = tmp1 + tmp2
            max_ind  = nums.index(max(nums))

            nums.reverse()
            k = len(nums)
            new.append(k)

            nums.pop()