# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def find_target_inc(start, end, target):
            low = start - 1
            high = end + 1
            
            while low < high-1:
                mid = ((low+high) // 2)
                if mid not in self.memo:
                    self.memo[mid] = mountain_arr.get(mid)

                if self.memo[mid] == target:
                    return mid
                
                elif self.memo[mid] < target: 
                    low = mid
                    
                else:
                    high = mid
                    
            return -1
        
        def find_target_dec(start, end, target):
            low = start - 1
            high = end
            
            while low < high-1:
                mid = ((low+high) // 2)

                if mid not in self.memo:
                    self.memo[mid] = mountain_arr.get(mid)

                if self.memo[mid] == target:
                    return mid
                
                elif self.memo[mid] > target: 
                    low = mid
                    
                else:
                    high = mid

            return -1

        def find_mountain_index():
            n = mountain_arr.length()
            low = -1
            high = n

            while low < high-1:
                mid = ((low+high) // 2)
                
                if mid-1 not in self.memo and mid > 0:
                    self.memo[mid-1] = mountain_arr.get(mid-1)
                    
                if mid not in self.memo:
                    self.memo[mid] = mountain_arr.get(mid)
                    
                if mid+1 not in self.memo and mid < n-1:
                    self.memo[mid+1] = mountain_arr.get(mid+1)

                # if is the mountain
                if (mid == 0 or self.memo[mid] > self.memo[mid-1]) and (mid == n-1 or self.memo[mid] > self.memo[mid+1]):
                    return mid

                # if its increasing side
                elif (mid == 0 or self.memo[mid] > self.memo[mid-1]) and (mid == n-1 or self.memo[mid] < self.memo[mid+1]):
                    low = mid

                # if its decreasing side
                elif (mid == 0 or self.memo[mid] < self.memo[mid-1]) and (mid == n-1 or self.memo[mid] > self.memo[mid+1]):
                    high = mid

                    
        self.memo = {}
        size = mountain_arr.length()
        mountain_index = find_mountain_index()
        found_inc = find_target_inc(0, mountain_index, target)
        found_dec = find_target_dec(mountain_index, size, target)
        
        if found_inc == -1 and found_dec == -1:
            return -1
        
        if found_inc != -1:
            return found_inc
        
        return found_dec