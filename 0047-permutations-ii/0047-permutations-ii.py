class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        self.ans = []
        self.set_ = set()
        size = len(nums)
        def backtrack(arr, path):
            if len(path) >= size and tuple(path) not in self.set_:
                self.ans.append(path)
                self.set_.add(tuple(path))
                return

            for i in range(len(arr)):
                new_arr = arr[:]
                new_arr.remove(arr[i])
                backtrack(new_arr, path[:]+[arr[i]])
                
        backtrack(nums[:], [])
        return self.ans