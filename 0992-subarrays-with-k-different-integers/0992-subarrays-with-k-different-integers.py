class Solution:
    def subarraysWithKDistinct(self, nums ,k) -> int:
        #until there are k unique numbers u go right
        #then u keep going right until u find the (k+1)th unique element but
        #this time u keep incrementing ur result
        #when u do find the (k+1)th ele then u start shrinking from left and 
        #incrementing until the unique numbers become (k+1) then u repeat the process
        
        
        left = right = 0
        n = len(nums)
        unique = {}
        accumulator = 0
        while right < n:

            if len(unique) <= k:
                if nums[right] in unique:
                    unique[nums[right]] += 1

                else:
                    unique[nums[right]] = 1


            if len(unique) == k:
                accumulator += 1
                uCopy = unique.copy()
                newAccumulator = self.shrinkAndReset(left,uCopy,k,nums)
                accumulator += newAccumulator

                right += 1

            elif len(unique) >= k:
                unique.pop(nums[right])
                while len(unique) == k:
                    if unique[nums[left]] == 1:
                        unique.pop(nums[left])

                    else:
                        unique[nums[left]] -= 1

                    left += 1

            else:
                right += 1

        return accumulator

    def shrinkAndReset(self,left,unique,k,nums):
        curAccumulator = 0

        while len(unique)==k:
            if unique[nums[left]] == 1:
                unique.pop(nums[left])

            else:
                unique[nums[left]] -= 1
            left += 1

            if len(unique) == k:
                curAccumulator += 1


        return curAccumulator